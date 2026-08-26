"""
voice_engine.py – STT (Faster-Whisper) + TTS (gTTS/Piper)
"""
import asyncio, base64, io, os, tempfile
from pathlib import Path
from typing import Optional
from backend.config import settings, AUDIO_DIR


class VoiceEngine:
    def __init__(self):
        self._whisper_model = None
        self._tts_engine = "gtts"  # gtts | piper

    def _load_whisper(self):
        if self._whisper_model is None:
            try:
                from faster_whisper import WhisperModel
                self._whisper_model = WhisperModel(
                    settings.WHISPER_MODEL, device="cpu", compute_type="int8"
                )
            except ImportError:
                self._whisper_model = None
        return self._whisper_model

    # ── SPEECH TO TEXT ────────────────────────────────────────────────────────
    async def transcribe(self, audio_data: bytes, language: str = "en") -> dict:
        """Convert audio to text using Faster-Whisper."""
        def _do_transcribe():
            model = self._load_whisper()
            if model is None:
                return {"text": "", "language": language, "error": "Whisper not available"}
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
                f.write(audio_data)
                tmp_path = f.name
            try:
                segments, info = model.transcribe(tmp_path, language=language, beam_size=5)
                text = " ".join(seg.text.strip() for seg in segments)
                return {"text": text.strip(), "language": info.language, "error": None}
            finally:
                os.unlink(tmp_path)

        return await asyncio.to_thread(_do_transcribe)

    async def transcribe_base64(self, audio_b64: str, language: str = "en") -> dict:
        """Transcribe audio from base64 string."""
        try:
            audio_bytes = base64.b64decode(audio_b64)
            return await self.transcribe(audio_bytes, language)
        except Exception as e:
            return {"text": "", "language": language, "error": str(e)}

    # ── TEXT TO SPEECH ────────────────────────────────────────────────────────
    async def synthesize(self, text: str, language: str = "en",
                          filename: Optional[str] = None) -> Optional[str]:
        """Convert text to speech, return audio file path."""
        def _do_tts():
            try:
                out_file = AUDIO_DIR / (filename or f"tts_{hash(text)}.wav")
                if self._tts_engine == "piper":
                    import wave
                    from piper.voice import PiperVoice
                    # Requires model in data/piper_models folder
                    model_path = BASE_DIR / "data" / "piper_models" / f"{language}.onnx"
                    if not model_path.exists():
                        raise FileNotFoundError(f"Piper model not found at {model_path}")
                    voice = PiperVoice.load(str(model_path))
                    with wave.open(str(out_file), 'wb') as wav_file:
                        voice.synthesize(text, wav_file)
                    return str(out_file)
                else:
                    from gtts import gTTS
                    out_file = AUDIO_DIR / (filename or f"tts_{hash(text)}.mp3")
                    tts = gTTS(text=text, lang=language, slow=False)
                    tts.save(str(out_file))
                    return str(out_file)
            except Exception as e:
                print(f"TTS Error: {e}")
                return None

        return await asyncio.to_thread(_do_tts)

    async def synthesize_to_base64(self, text: str, language: str = "en") -> Optional[str]:
        """Convert text to speech, return base64 audio with caching."""
        def _do_tts():
            try:
                # Use a stable hash for caching
                import hashlib
                text_hash = hashlib.md5(text.encode('utf-8')).hexdigest()
                
                if self._tts_engine == "piper":
                    out_file = AUDIO_DIR / f"tts_{text_hash}.wav"
                    if not out_file.exists():
                        import wave
                        from piper.voice import PiperVoice
                        model_path = BASE_DIR / "data" / "piper_models" / f"{language}.onnx"
                        if not model_path.exists():
                            raise FileNotFoundError(f"Piper model not found at {model_path}")
                        voice = PiperVoice.load(str(model_path))
                        with wave.open(str(out_file), 'wb') as wav_file:
                            voice.synthesize(text, wav_file)
                            
                    with open(out_file, "rb") as f:
                        return base64.b64encode(f.read()).decode("utf-8")
                else:
                    out_file = AUDIO_DIR / f"tts_{text_hash}.mp3"
                    if not out_file.exists():
                        from gtts import gTTS
                        tts = gTTS(text=text, lang=language, slow=False)
                        tts.save(str(out_file))
                        
                    with open(out_file, "rb") as f:
                        return base64.b64encode(f.read()).decode("utf-8")
            except Exception as e:
                print(f"TTS B64 Error: {e}")
                return None
        return await asyncio.to_thread(_do_tts)


voice_engine = VoiceEngine()
