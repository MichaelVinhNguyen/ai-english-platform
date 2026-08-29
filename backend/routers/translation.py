from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.database.models import User
from backend.database.schemas import TranslateResult
from backend.services.ai_engine import ai_engine
from backend.routers.auth import get_current_user

translation_router = APIRouter(prefix="/api/translation", tags=["Translation"])

class DetailedTranslateRequest(BaseModel):
    text: str
    source_lang: str = "en"
    target_lang: str = "vi"
    mode: str = "natural" # literal, natural, business, academic
    detailed: bool = True

@translation_router.post("/translate")
async def translate(data: DetailedTranslateRequest, current_user: User = Depends(get_current_user)):
    mode_instructions = {
        "literal": "Dịch sát từng từ nghĩa đen (Literal Translation).",
        "natural": "Dịch mượt mà, tự nhiên chuẩn bản xứ (Natural Translation).",
        "business": "Dịch theo trang trọng, chuyên nghiệp thương mại (Business/Corporate Translation).",
        "academic": "Dịch theo văn phong hàn lâm, học thuật (Academic/Research Translation)."
    }
    instruction = mode_instructions.get(data.mode, mode_instructions["natural"])
    
    prompt = f"""Hãy dịch đoạn văn sau từ {data.source_lang} sang {data.target_lang} theo tiêu chuẩn: {instruction}
Văn bản: "{data.text}"

Format JSON:
{{
  "translated": "Bản dịch theo chế độ {data.mode}",
  "mode": "{data.mode}",
  "explanation": "Giải thích cấu trúc và lựa chọn từ vựng",
  "examples": ["Ví dụ ngữ cảnh 1", "Ví dụ ngữ cảnh 2"],
  "synonyms": ["Từ đồng nghĩa/cách diễn đạt thay thế"],
  "grammar_notes": "Ghi chú ngữ pháp đáng chú ý"
}}"""
    try:
        resp = await ai_engine._generate_text(prompt)
        import json
        res = json.loads(ai_engine._extract_json(resp.text))
        return {
            "original": data.text,
            "translated": res.get("translated", ""),
            "mode": data.mode,
            "source_lang": data.source_lang,
            "target_lang": data.target_lang,
            "explanation": res.get("explanation"),
            "examples": res.get("examples"),
            "synonyms": res.get("synonyms"),
            "grammar_notes": res.get("grammar_notes")
        }
    except Exception:
        fallback = await ai_engine.translate(data.text, data.source_lang, data.target_lang, data.detailed)
        return {
            "original": data.text,
            "translated": fallback.get("translated", ""),
            "mode": data.mode,
            "source_lang": data.source_lang,
            "target_lang": data.target_lang,
            "explanation": fallback.get("explanation"),
            "examples": fallback.get("examples"),
            "synonyms": fallback.get("synonyms")
        }

@translation_router.post("/quick")
async def quick_translate(text: str, current_user: User = Depends(get_current_user)):
    result = await ai_engine.translate(text, "en", "vi")
    return {"original": text, "translated": result.get("translated", "")}


@translation_router.get("/exercises")
async def get_translation_exercises(level: Optional[str] = None, current_user: User = Depends(get_current_user)):
    """Trả về danh sách 35+ bài tập luyện dịch chuyên sâu Anh-Việt & Việt-Anh."""
    exercises = [
        # A1 - A2
        {
            "id": 1, "title": "Bài 1: Giới Thiệu Bản Thân & Quê Hương", "level": "A1", "direction": "en_to_vi",
            "source_text": "Hello, my name is Alex and I am a software engineer from Da Nang. I love reading books and drinking coffee every morning.",
            "reference_translation": "Xin chào, tôi tên là Alex và tôi là một kỹ sư phần mềm đến từ Đà Nẵng. Tôi thích đọc sách và uống cà phê mỗi buổi sáng.",
            "notes": "Lưu ý cấu trúc 'love doing something' (thích làm gì) và thì hiện tại đơn."
        },
        {
            "id": 2, "title": "Bài 2: Đặt Món Tại Nhà Hàng", "level": "A1", "direction": "vi_to_en",
            "source_text": "Làm ơn cho tôi một đĩa mì Ý hải sản và một ly nước cam ép.",
            "reference_translation": "Please give me a plate of seafood spaghetti and a glass of fresh orange juice.",
            "notes": "Dùng cấu trúc lịch sự 'Please give me...' hoặc 'I would like to have...'."
        },
        {
            "id": 3, "title": "Bài 3: Chỉ Đường Trong Thành Phố", "level": "A1", "direction": "en_to_vi",
            "source_text": "Go straight down this street for two blocks, then turn left at the traffic light. The post office is on your right.",
            "reference_translation": "Đi thẳng theo con đường này qua hai dãy nhà, sau đó rẽ trái tại cột đèn giao thông. Bưu điện nằm ở phía bên tay phải của bạn.",
            "notes": "Cụm từ chỉ phương hướng: 'turn left at', 'on your right'."
        },
        {
            "id": 4, "title": "Bài 4: Kể Về Thói Quen Hàng Ngày", "level": "A2", "direction": "vi_to_en",
            "source_text": "Mỗi ngày tôi thức dậy lúc 6 giờ sáng, tập thể dục 30 phút và sau đó chuẩn bị đi làm.",
            "reference_translation": "Every day I wake up at 6:00 AM, exercise for 30 minutes, and then get ready for work.",
            "notes": "Chú ý giới từ thời gian: 'at 6:00 AM' và 'for 30 minutes'."
        },
        {
            "id": 5, "title": "Bài 5: Đặt Phòng Khách Sạn", "level": "A2", "direction": "en_to_vi",
            "source_text": "I would like to book a deluxe double room with sea view for three nights, including breakfast.",
            "reference_translation": "Tôi muốn đặt một phòng đôi cao cấp có tầm nhìn hướng biển trong ba đêm, đã bao gồm bữa sáng.",
            "notes": "'Sea view' dịch mượt mà là 'hướng biển' hoặc 'tầm nhìn ra biển'."
        },
        {
            "id": 6, "title": "Bài 6: Mô Tả Sở Thích Cuối Tuần", "level": "A2", "direction": "vi_to_en",
            "source_text": "Vào những ngày cuối tuần, tôi thường đi dã ngoại cùng gia đình ở vùng ngoại ô để tận hưởng không khí trong lành.",
            "reference_translation": "On weekends, I usually go on a picnic with my family in the suburbs to enjoy the fresh air.",
            "notes": "Dùng cụm 'in the suburbs' (ở vùng ngoại ô) và 'enjoy the fresh air'."
        },
        # B1
        {
            "id": 7, "title": "Bài 7: Phỏng Vấn Xin Việc", "level": "B1", "direction": "en_to_vi",
            "source_text": "My greatest strength is my problem-solving ability and my willingness to learn new emerging technologies rapidly.",
            "reference_translation": "Điểm mạnh lớn nhất của tôi là khả năng giải quyết vấn đề và sự sẵn sàng học hỏi các công nghệ mới nổi một cách nhanh chóng.",
            "notes": "'Emerging technologies' = các công nghệ mới nổi / tiên tiến."
        },
        {
            "id": 8, "title": "Bài 8: Email Xin Phép Nghỉ Ốm", "level": "B1", "direction": "vi_to_en",
            "source_text": "Tôi viết email này để xin phép nghỉ làm hôm nay do bị sốt cao. Tôi sẽ cố gắng kiểm tra email khẩn cấp từ nhà.",
            "reference_translation": "I am writing this email to request sick leave today due to a high fever. I will try to check urgent emails from home.",
            "notes": "Thuật ngữ 'request sick leave' (xin nghỉ ốm) và 'due to a high fever'."
        },
        {
            "id": 9, "title": "Bài 9: Giới Thiệu Tính Năng Sản Phẩm Mới", "level": "B1", "direction": "en_to_vi",
            "source_text": "Our new mobile application allows users to track their daily expenses and set customized monthly savings budgets seamlessly.",
            "reference_translation": "Ứng dụng di động mới của chúng tôi cho phép người dùng theo dõi các khoản chi tiêu hàng ngày và thiết lập ngân sách tiết kiệm hàng tháng tùy chỉnh một cách liền mạch.",
            "notes": "'Seamlessly' = một cách mượt mà / liền mạch."
        },
        {
            "id": 10, "title": "Bài 10: Thông Báo Hoãn Chuyến Bay", "level": "B1", "direction": "vi_to_en",
            "source_text": "Do điều kiện thời tiết xấu, chuyến bay VN123 sẽ bị hoãn lại 45 phút. Chúng tôi thành thật xin lỗi vì sự bất tiện này.",
            "reference_translation": "Due to adverse weather conditions, flight VN123 will be delayed by 45 minutes. We sincerely apologize for this inconvenience.",
            "notes": "'Adverse weather conditions' = điều kiện thời tiết xấu/bất lợi."
        },
        {
            "id": 11, "title": "Bài 11: Lợi Ích Của Năng Lượng Tái Tạo", "level": "B1", "direction": "en_to_vi",
            "source_text": "Transitioning to solar and wind energy significantly reduces greenhouse gas emissions and mitigates global warming.",
            "reference_translation": "Chuyển dịch sang năng lượng mặt trời và gió giúp giảm đáng kể lượng phát thải khí nhà kính và giảm thiểu hiện tượng nóng lên toàn cầu.",
            "notes": "'Mitigate' = giảm nhẹ / giảm thiểu."
        },
        {
            "id": 12, "title": "Bài 12: Thói Quen Đọc Sách Phát Triển Bản Thân", "level": "B1", "direction": "vi_to_en",
            "source_text": "Việc đọc sách 20 phút mỗi ngày giúp mở rộng vốn từ vựng và nâng cao khả năng tập trung của não bộ.",
            "reference_translation": "Reading books for 20 minutes daily helps expand vocabulary and enhance the brain's concentration ability.",
            "notes": "Dùng danh động từ 'Reading books...' làm chủ ngữ."
        },
        # B2
        {
            "id": 13, "title": "Bài 13: Trí Tuệ Nhân Tạo & Tự Động Hóa", "level": "B2", "direction": "en_to_vi",
            "source_text": "Artificial intelligence algorithms are revolutionizing diagnostic radiology by detecting microscopic tumors earlier than conventional methods.",
            "reference_translation": "Các thuật toán trí tuệ nhân tạo đang cách mạng hóa ngành chẩn đoán X-quang/hình ảnh học bằng cách phát hiện các khối u siêu nhỏ sớm hơn các phương pháp thông thường.",
            "notes": "'Diagnostic radiology' = chẩn đoán hình ảnh học."
        },
        {
            "id": 14, "title": "Bài 14: Báo Cáo Tài Chính Doanh Nghiệp", "level": "B2", "direction": "vi_to_en",
            "source_text": "Lợi nhuận ròng của công ty trong quý 3 tăng 25% nhờ vào việc tối ưu hóa chi phí vận hành và mở rộng thị phần quốc tế.",
            "reference_translation": "The company's net profit in the third quarter increased by 25% thanks to optimizing operating expenses and expanding international market share.",
            "notes": "'Net profit' = lợi nhuận ròng; 'operating expenses' = chi phí vận hành."
        },
        {
            "id": 15, "title": "Bài 15: Biến Đổi Khí Hậu & Nước Biển Dâng", "level": "B2", "direction": "en_to_vi",
            "source_text": "Rising sea levels threaten low-lying coastal communities, necessitating substantial investments in flood barriers and resilient infrastructure.",
            "reference_translation": "Mực nước biển dâng cao đe dọa các cộng đồng ven biển vùng trũng thấp, đòi hỏi những khoản đầu tư đáng kể vào các đê ngăn triều cường và cơ sở hạ tầng kiên cố.",
            "notes": "'Resilient infrastructure' = cơ sở hạ tầng có khả năng chống chịu/kiên cố."
        },
        {
            "id": 16, "title": "Bài 16: Tranh Biện Làm Việc Từ Xa", "level": "B2", "direction": "vi_to_en",
            "source_text": "Mặc dù làm việc từ xa mang lại sự linh hoạt tuyệt vời, nó cũng đòi hỏi kỷ luật tự giác cao và kỹ năng quản lý thời gian hiệu quả.",
            "reference_translation": "Although remote work offers exceptional flexibility, it also demands high self-discipline and effective time management skills.",
            "notes": "Dùng liên từ 'Although / While'."
        },
        {
            "id": 17, "title": "Bài 17: Kinh Tế Tuần Hoàn", "level": "B2", "direction": "en_to_vi",
            "source_text": "The circular economy replaces the traditional linear manufacturing model by designing products for durability, reuse, and closed-loop recycling.",
            "reference_translation": "Kinh tế tuần hoàn thay thế mô hình sản xuất tuyến tính truyền thống bằng cách thiết kế các sản phẩm phục vụ độ bền, tái sử dụng và tái chế khép kín.",
            "notes": "'Closed-loop recycling' = tái chế vòng kín / khép kín."
        },
        {
            "id": 18, "title": "Bài 18: Tâm Lý Học Hành Vi & Quyết Định Tài Chính", "level": "B2", "direction": "vi_to_en",
            "source_text": "Thiên kiến ác cảm mất mát khiến các nhà đầu tư thường có xu hướng giữ lại các khoản đầu tư thua lỗ quá lâu thay vì cắt lỗ dứt khoát.",
            "reference_translation": "Loss aversion bias leads investors to hold onto losing investments for too long rather than decisively cutting losses.",
            "notes": "'Loss aversion bias' = thiên kiến ác cảm mất mát."
        },
        # C1
        {
            "id": 19, "title": "Bài 19: Tính Dẻo Não Bộ (Neuroplasticity)", "level": "C1", "direction": "en_to_vi",
            "source_text": "Neuroplasticity demonstrates that cognitive training and lifelong bilingualism construct robust cognitive reserve, mitigating neurodegenerative decline.",
            "reference_translation": "Tính dẻo của não bộ chứng minh rằng rèn luyện nhận thức và sử dụng song ngữ suốt đời xây dựng nên nguồn dự trữ nhận thức vững chắc, giúp giảm thiểu sự suy thoái thần kinh.",
            "notes": "'Cognitive reserve' = nguồn dự trữ nhận thức."
        },
        {
            "id": 20, "title": "Bài 20: Địa Chính Trị Khoáng Sản Đất Hiếm", "level": "C1", "direction": "vi_to_en",
            "source_text": "Sự phụ thuộc quá mức vào một chuỗi cung ứng khoáng sản đất hiếm duy nhất có thể gây ra những rủi ro an ninh kinh tế nghiêm trọng cho tiến trình chuyển đổi xanh.",
            "reference_translation": "Over-reliance on a single critical rare earth mineral supply chain poses severe economic security vulnerabilities for the green transition.",
            "notes": "'Over-reliance on' = sự phụ thuộc quá mức vào."
        },
        {
            "id": 21, "title": "Bài 21: Mật Mã Học Hậu Lượng Tử", "level": "C1", "direction": "en_to_vi",
            "source_text": "Quantum computers exploiting Shor's algorithm threaten to compromise classical asymmetric encryption, accelerating the adoption of post-quantum cryptography.",
            "reference_translation": "Máy tính lượng tử khai thác thuật toán Shor đe dọa phá vỡ hệ thống mã hóa bất đối xứng cổ điển, thúc đẩy việc áp dụng nhanh chóng mật mã học hậu lượng tử.",
            "notes": "'Asymmetric encryption' = mã hóa bất đối xứng."
        },
        {
            "id": 22, "title": "Bài 22: Đạo Đức Chỉnh Sửa Gen CRISPR", "level": "C1", "direction": "vi_to_en",
            "source_text": "Việc biến đổi gen dòng mầm ở người làm dấy lên những tình thế tiến thoái lưỡng nan sâu sắc về mặt đạo đức liên quan đến các đột biến ngoài ý muốn.",
            "reference_translation": "Human germline genetic modification precipitates profound bioethical dilemmas regarding unintended off-target mutational cascades.",
            "notes": "'Germline modification' = biến đổi dòng mầm; 'off-target mutations' = đột biến ngoài ý muốn/ngoài mục tiêu."
        },
        {
            "id": 23, "title": "Bài 23: Chính Sách Tiền Tệ & Lạm Phát Vĩ Mô", "level": "C1", "direction": "en_to_vi",
            "source_text": "Central banks must calibrate interest rate hikes with precision to curb inflationary expectations without precipitating prolonged economic recessions.",
            "reference_translation": "Các ngân hàng trung ương phải cân chỉnh các đợt tăng lãi suất một cách chuẩn xác nhằm kiềm chế kỳ vọng lạm phát mà không gây ra những cuộc suy thoái kinh tế kéo dài.",
            "notes": "'Calibrate with precision' = cân chỉnh chuẩn xác; 'curb' = kiềm chế."
        },
        {
            "id": 24, "title": "Bài 24: Kiến Trúc Đô Thị & Biophilic Design", "level": "C1", "direction": "vi_to_en",
            "source_text": "Bằng cách tích hợp các khu rừng thẳng đứng và ánh sáng tự nhiên, kiến trúc ưa sinh học giúp giảm hiệu ứng đảo nhiệt đô thị và cải thiện sức khỏe tinh thần.",
            "reference_translation": "By integrating vertical forests and natural daylighting, biophilic architecture mitigates the urban heat island effect and enhances psychological well-being.",
            "notes": "'Biophilic architecture' = kiến trúc ưa sinh học; 'urban heat island effect' = hiệu ứng đảo nhiệt đô thị."
        },
        # C2
        {
            "id": 25, "title": "Bài 25: Nhận Thức Luận Siêu Nghiệm Của Kant", "level": "C2", "direction": "en_to_vi",
            "source_text": "Kant's transcendental idealism posited that space and time are not ontological realities, but subjective a priori intuitions structuring human phenomenal experience.",
            "reference_translation": "Chủ nghĩa duy tâm siêu nghiệm của Kant khẳng định rằng không gian và thời gian không phải là các thực tại hữu thể học, mà là những trực quan tiên nghiệm chủ quan kiến tạo nên trải nghiệm hiện tượng của con người.",
            "notes": "Thuật ngữ triết học: 'ontological realities' (thực tại hữu thể học), 'a priori intuitions' (trực quan tiên nghiệm)."
        },
        {
            "id": 26, "title": "Bài 26: Vấn Đề Căn Chỉnh Trí Tuệ Nhân Tạo (AGI Alignment)", "level": "C2", "direction": "vi_to_en",
            "source_text": "Thuyết hội tụ công cụ dự đoán rằng các tác nhân siêu thông minh sẽ tất yếu theo đuổi các mục tiêu phụ như bảo tồn mục tiêu và tích lũy tài nguyên không kiểm soát.",
            "reference_translation": "Instrumental convergence posits that superintelligent agents will inevitably pursue intermediate sub-objectives, such as goal integrity and unchecked resource acquisition.",
            "notes": "'Instrumental convergence' = thuyết hội tụ công cụ; 'goal integrity' = tính toàn vẹn mục tiêu."
        },
        {
            "id": 27, "title": "Bài 27: Lý Thuyết Hỗn Loạn & Tập Hút Kỳ Lạ", "level": "C2", "direction": "en_to_vi",
            "source_text": "Trajectories within deterministic chaotic systems never intersect, asymptotically settling onto strange attractors with fractional fractal dimensions.",
            "reference_translation": "Các quỹ đạo bên trong các hệ thống hỗn loạn tất định không bao giờ cắt nhau, tiệm cận dần vào các tập hút kỳ lạ với số chiều fractal phân số.",
            "notes": "'Strange attractors' = tập hút kỳ lạ; 'fractional fractal dimensions' = số chiều fractal phân số."
        },
        {
            "id": 28, "title": "Bài 28: Ký Hiệu Học Giải Cấu Trúc (Deconstruction)", "level": "C2", "direction": "vi_to_en",
            "source_text": "Khái niệm 'différance' của Derrida chứng minh rằng ý nghĩa ngôn ngữ luôn bị trì hoãn vô tận và phân hóa liên tục bên trong các hệ thống ký hiệu.",
            "reference_translation": "Derrida's concept of 'différance' demonstrates that linguistic signification is perpetually deferred and differentiated within sign systems.",
            "notes": "'Perpetually deferred' = luôn bị trì hoãn vô tận."
        },
        {
            "id": 29, "title": "Bài 29: Dấu Ấn Sinh Học Trên Ngoại Hành Tinh", "level": "C2", "direction": "en_to_vi",
            "source_text": "The simultaneous atmospheric detection of methane and molecular oxygen in chemical disequilibrium serves as a compelling exoplanetary biosignature.",
            "reference_translation": "Sự phát hiện đồng thời khí mê-tan và oxy phân tử ở trạng thái mất cân bằng hóa học trong khí quyển đóng vai trò như một dấu ấn sinh học ngoại hành tinh đầy thuyết phục.",
            "notes": "'Chemical disequilibrium' = mất cân bằng hóa học; 'biosignature' = dấu ấn sinh học."
        },
        {
            "id": 30, "title": "Bài 30: Luật Biển Quốc Tế & Hải Hành Bắc Cực", "level": "C2", "direction": "vi_to_en",
            "source_text": "Sự tan băng nhanh chóng ở lưu vực Bắc Cực đã làm bùng phát các tranh chấp quyền tài phán gay gắt theo Công ước Liên Hợp Quốc về Luật Biển (UNCLOS).",
            "reference_translation": "Accelerating cryospheric thawing in the Arctic basin has ignited contentious jurisdictional disputes under the United Nations Convention on the Law of the Sea (UNCLOS).",
            "notes": "'Cryospheric thawing' = sự tan băng quyển; 'contentious jurisdictional disputes' = tranh chấp quyền tài phán gay gắt."
        },
        {
            "id": 31, "title": "Bài 31: Kinh Tế Lượng & Chuỗi Thời Gian Phi Dừng", "level": "C2", "direction": "en_to_vi",
            "source_text": "Econometricians employ vector autoregression and cointegration tests to analyze non-stationary macroeconomic time series and prevent spurious regression.",
            "reference_translation": "Các nhà kinh tế lượng sử dụng mô hình tự hồi quy vector và kiểm định đồng liên kết để phân tích chuỗi thời gian kinh tế vĩ mô phi dừng và ngăn ngừa hồi quy giả tạo.",
            "notes": "'Spurious regression' = hồi quy giả tạo / hồi quy ngụy biện."
        },
        {
            "id": 32, "title": "Bài 32: Động Học Phân Tử & Gấp Cuộn Protein", "level": "C2", "direction": "vi_to_en",
            "source_text": "Các mô hình học sâu như AlphaFold đã giải quyết bài toán gấp cuộn protein kéo dài 50 năm bằng cách dự đoán cấu trúc 3D với độ chính xác cấp độ nguyên tử.",
            "reference_translation": "Deep learning models such as AlphaFold have resolved the 50-year-old protein folding challenge by predicting 3D structures with atomic-level accuracy.",
            "notes": "'Protein folding challenge' = bài toán gấp cuộn protein; 'atomic-level accuracy' = độ chính xác cấp độ nguyên tử."
        },
        {
            "id": 33, "title": "Bài 33: Siêu Dẫn Nhiệt Độ Cao", "level": "C2", "direction": "en_to_vi",
            "source_text": "Achieving ambient-pressure room-temperature superconductivity would revolutionize power transmission grids by eradicating electrical resistance losses entirely.",
            "reference_translation": "Đạt được hiện tượng siêu dẫn ở nhiệt độ phòng và áp suất thường sẽ cách mạng hóa các lưới truyền tải điện năng bằng cách triệt tiêu hoàn toàn tổn thất do điện trở.",
            "notes": "'Ambient-pressure room-temperature superconductivity' = siêu dẫn nhiệt độ phòng áp suất thường."
        },
        {
            "id": 34, "title": "Bài 34: Thuyết Đa Vũ Trụ & Cơ Học Lượng Tử", "level": "C2", "direction": "vi_to_en",
            "source_text": "Cách diễn giải nhiều thế giới của cơ học lượng tử phủ nhận sự sụp đổ của hàm sóng, cho rằng mọi kết quả lượng tử khả dĩ đều diễn ra trong các nhánh vũ trụ song song.",
            "reference_translation": "The many-worlds interpretation of quantum mechanics rejects wave function collapse, asserting that all possible quantum outcomes manifest in parallel branching universes.",
            "notes": "'Wave function collapse' = sự sụp đổ hàm sóng; 'many-worlds interpretation' = cách diễn giải nhiều thế giới."
        },
        {
            "id": 35, "title": "Bài 35: Hợp Đồng Thương Mại Quốc Tế & Điều Khoản Bất Khả Kháng", "level": "C2", "direction": "en_to_vi",
            "source_text": "The invocation of the force majeure clause requires rigorous legal substantiation demonstrating that contractual non-performance resulted from unforeseeable, insurmountable external events.",
            "reference_translation": "Việc viện dẫn điều khoản bất khả kháng đòi hỏi chứng cứ pháp lý chặt chẽ chứng minh rằng việc không thực hiện nghĩa vụ hợp đồng là do các sự kiện ngoại cảnh không thể lường trước và không thể vượt qua.",
            "notes": "'Force majeure clause' = điều khoản bất khả kháng; 'contractual non-performance' = không thực hiện nghĩa vụ hợp đồng."
        }
    ]
    if level:
        exercises = [e for e in exercises if e["level"] == level]
    return {"exercises": exercises, "total": len(exercises)}


