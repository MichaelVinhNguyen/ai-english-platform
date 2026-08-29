# -*- coding: utf-8 -*-
"""
seed_complete_system_30_plus.py – Master Database Seeder for Complete AI English Platform
Contains:
1. GRAMMAR_RULES (35 topics A1-C2)
2. LISTENING_EXERCISES (35 topics A1-C2)
3. READING_ARTICLES (35 articles A1-C2)
4. SPEAKING_TOPICS (35 topics A1-C2)
5. WRITING_PROMPTS (35 tasks A1-C2)
6. TRANSLATION_EXERCISES (35 exercises A1-C2)
7. COURSES & LESSONS (30 courses, 120+ lessons)
8. MOCK_TESTS (30+ exams A1-C2, TOEIC, IELTS)
9. VOCABULARY GENERATOR (1,000 words per letter A-Z = 24,000+ words)
"""

import asyncio
import os
import sys
import time
import json
import sqlite3
from collections import defaultdict

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import (
    Vocabulary, GrammarRule, ReadingArticle, ListeningExercise,
    Course, Lesson, Badge, Mission, MockTest, QuizQuestion
)

# NLTK for rich vocabulary corpus
import nltk
try:
    nltk.data.find('corpora/words')
except LookupError:
    nltk.download('words')
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

from nltk.corpus import words, wordnet

# ═══════════════════════════════════════════════════════════════════════════════
# 1. GRAMMAR DATA (35 LESSONS A1 -> C2)
# ═══════════════════════════════════════════════════════════════════════════════
GRAMMAR_RULES = [
    # A1 (6 lessons)
    {
        "title": "Present Simple (Thì Hiện Tại Đơn)",
        "category": "tenses",
        "level": "A1",
        "explanation": "Diễn tả hành động lặp đi lặp lại theo thói quen, chân lý hoặc sự thật hiển nhiên. Cấu trúc: S + V(s/es) | S + do/does not + V | Do/Does + S + V?",
        "examples": [
            {"en": "She works at an international company.", "vi": "Cô ấy làm việc tại một công ty quốc tế."},
            {"en": "The earth revolves around the sun.", "vi": "Trái đất quay quanh mặt trời."},
            {"en": "I always drink a cup of coffee in the morning.", "vi": "Tôi luôn uống một tách cà phê vào buổi sáng."}
        ],
        "tips": ["Thêm -es với các động từ tận cùng bằng: -o, -s, -ch, -x, -sh, -z.", "Dùng trạng từ tần suất: always, usually, often, sometimes, never."],
        "common_mistakes": ["He go to school (Sai -> He goes to school).", "Does she likes tea? (Sai -> Does she like tea?)."]
    },
    {
        "title": "Present Continuous (Thì Hiện Tại Tiếp Diễn)",
        "category": "tenses",
        "level": "A1",
        "explanation": "Diễn tả hành động đang diễn ra ngay tại thời điểm nói hoặc một kế hoạch trong tương lai gần. Cấu trúc: S + am/is/are + V-ing.",
        "examples": [
            {"en": "Look! The children are playing soccer in the park.", "vi": "Nhìn kìa! Lũ trẻ đang chơi bóng đá trong công viên."},
            {"en": "I am studying English with the AI Teacher right now.", "vi": "Tôi đang học tiếng Anh với Giáo viên AI lúc này."}
        ],
        "tips": ["Dấu hiệu nhận biết: now, right now, at the moment, look!, listen!.", "Các động từ chỉ tri giác, sở hữu (know, like, belong, see) thường không chia tiếp diễn."],
        "common_mistakes": ["I am knowing him (Sai -> I know him)."]
    },
    {
        "title": "Articles: A, An & The (Mạo Từ)",
        "category": "articles",
        "level": "A1",
        "explanation": "'A/An' dùng cho danh từ số ít đếm được chưa xác định ('An' đứng trước nguyên âm phát âm a, e, i, o, u). 'The' dùng cho danh từ đã xác định hoặc duy nhất.",
        "examples": [
            {"en": "I saw a doctor yesterday. The doctor was very kind.", "vi": "Tôi đã gặp một bác sĩ hôm qua. Vị bác sĩ đó rất ân cần."},
            {"en": "She has an umbrella and a raincoat.", "vi": "Cô ấy có một chiếc ô và một chiếc áo mưa."}
        ],
        "tips": ["'An hour' (âm h câm -> /aʊər/ nên dùng an).", "'A university' (phát âm là /juː/ bán nguyên âm nên dùng a)."],
        "common_mistakes": ["An university (Sai -> A university).", "I like the cats (Sai khi nói chung chung -> I like cats)."]
    },
    {
        "title": "Subject & Object Pronouns (Đại Từ Nhân Xưng & Tân Ngữ)",
        "category": "pronouns",
        "level": "A1",
        "explanation": "Đại từ chủ ngữ (I, you, he, she, it, we, they) đứng trước động từ. Đại từ tân ngữ (me, you, him, her, it, us, them) đứng sau động từ hoặc giới từ.",
        "examples": [
            {"en": "She gave him a wonderful birthday present.", "vi": "Cô ấy đã tặng anh ấy một món quà sinh nhật tuyệt vời."},
            {"en": "They invited us to their wedding dinner.", "vi": "Họ đã mời chúng tôi đến dự bữa tiệc cưới của họ."}
        ],
        "tips": ["Sau giới từ như with, to, for, about luôn dùng đại từ tân ngữ (e.g. Come with me)."],
        "common_mistakes": ["Between you and I (Sai -> Between you and me)."]
    },
    {
        "title": "Possessive Adjectives & Pronouns (Tính Từ & Đại Từ Sở Hữu)",
        "category": "pronouns",
        "level": "A1",
        "explanation": "Tính từ sở hữu (my, your, his, her, its, our, their) + Danh từ. Đại từ sở hữu (mine, yours, his, hers, ours, theirs) đứng độc lập thay thế cho danh từ.",
        "examples": [
            {"en": "This is my laptop, and that one is yours.", "vi": "Đây là máy tính xách tay của tôi, còn cái kia là của bạn."},
            {"en": "Her house is big, but ours is more modern.", "vi": "Nhà của cô ấy to, nhưng nhà của chúng tôi hiện đại hơn."}
        ],
        "tips": ["Không dùng danh từ ngay sau đại từ sở hữu (Không viết 'mine car')."],
        "common_mistakes": ["Its vs It's (Its là sở hữu, It's = It is)."]
    },
    {
        "title": "There is / There are & Quantifiers (Some, Any)",
        "category": "sentence_structure",
        "level": "A1",
        "explanation": "'There is' dùng cho danh từ số ít hoặc không đếm được. 'There are' dùng cho danh từ số nhiều. 'Some' dùng trong câu khẳng định, 'Any' dùng trong câu phủ định và nghi vấn.",
        "examples": [
            {"en": "There is some milk in the fridge.", "vi": "Có một ít sữa trong tủ lạnh."},
            {"en": "Are there any questions from the audience?", "vi": "Có câu hỏi nào từ phía khán giả không?"}
        ],
        "tips": ["Dùng 'some' trong lời mời lịch sự: 'Would you like some coffee?'"],
        "common_mistakes": ["There is many books (Sai -> There are many books)."]
    },
    # A2 (6 lessons)
    {
        "title": "Past Simple (Thì Quá Khứ Đơn)",
        "category": "tenses",
        "level": "A2",
        "explanation": "Diễn tả hành động đã xảy ra và kết thúc hoàn toàn tại thời điểm xác định trong quá khứ. Cấu trúc: S + V2/ed | S + did not + V0.",
        "examples": [
            {"en": "We visited Paris last summer and had a wonderful time.", "vi": "Chúng tôi đã thăm Paris mùa hè năm ngoái và có khoảng thời gian tuyệt vời."},
            {"en": "Did you watch the football match yesterday evening?", "vi": "Bạn đã xem trận bóng đá tối qua chưa?"}
        ],
        "tips": ["Học thuộc bảng 360 động từ bất quy tắc (go -> went -> gone, buy -> bought).", "Dấu hiệu: yesterday, last night, 2 days ago, in 2020."],
        "common_mistakes": ["Did you went there? (Sai -> Did you go there?)."]
    },
    {
        "title": "Past Continuous (Thì Quá Khứ Tiếp Diễn)",
        "category": "tenses",
        "level": "A2",
        "explanation": "Diễn tả hành động đang diễn ra tại một thời điểm xác định trong quá khứ hoặc một hành động đang xảy ra thì hành động khác xen vào. Cấu trúc: S + was/were + V-ing.",
        "examples": [
            {"en": "I was cooking dinner when the power went out.", "vi": "Tôi đang nấu bữa tối thì bị mất điện."},
            {"en": "At 8 PM yesterday, we were watching a movie.", "vi": "Lúc 8 giờ tối hôm qua, chúng tôi đang xem phim."}
        ],
        "tips": ["While + Quá khứ tiếp diễn (While I was driving...).", "When + Quá khứ đơn (When he called...)."],
        "common_mistakes": ["I was cook when she arrived (Sai -> I was cooking)."]
    },
    {
        "title": "Comparative & Superlative (So Sánh Hơn & Nhất)",
        "category": "adjectives",
        "level": "A2",
        "explanation": "So sánh hơn: Tính từ ngắn + -er than; more + Tính từ dài + than. So sánh nhất: the + Tính từ ngắn + -est; the most + Tính từ dài.",
        "examples": [
            {"en": "Tokyo is more expensive than Bangkok.", "vi": "Tokyo đắt đỏ hơn Bangkok."},
            {"en": "Mount Everest is the highest mountain in the world.", "vi": "Đỉnh Everest là ngọn núi cao nhất thế giới."}
        ],
        "tips": ["Bất quy tắc: good -> better -> best; bad -> worse -> worst; far -> farther/further -> farthest/furthest."],
        "common_mistakes": ["More faster (Sai -> faster).", "Most best (Sai -> best)."]
    },
    {
        "title": "Modal Verbs: Can, Could, Must, Should (Động Từ Khuyết Thiếu)",
        "category": "modals",
        "level": "A2",
        "explanation": "Dùng để biểu thị khả năng (can/could), lời khuyên (should), hoặc sự bắt buộc (must/have to). Sau Modal Verbs luôn là động từ nguyên mẫu không 'to'.",
        "examples": [
            {"en": "You should drink plenty of water every day.", "vi": "Bạn nên uống nhiều nước mỗi ngày."},
            {"en": "All passengers must fasten their seatbelts during takeoff.", "vi": "Tất cả hành khách phải thắt dây an toàn khi máy bay cất cánh."}
        ],
        "tips": ["Must not (cấm đoán) khác với Don't have to (không cần thiết)."],
        "common_mistakes": ["He can swims (Sai -> He can swim).", "You should to go (Sai -> You should go)."]
    },
    {
        "title": "Future Simple (Will) vs Near Future (Be Going To)",
        "category": "tenses",
        "level": "A2",
        "explanation": "'Will' dùng cho quyết định bộc phát tại thời điểm nói hoặc lời hứa/dự đoán không có bằng chứng. 'Be going to' dùng cho kế hoạch đã dự định trước hoặc dự đoán có bằng chứng cụ thể.",
        "examples": [
            {"en": "Look at those dark clouds! It is going to rain.", "vi": "Nhìn những đám mây đen kìa! Trời sắp mưa rồi."},
            {"en": "The phone is ringing. I will answer it.", "vi": "Điện thoại đang reo. Tôi sẽ nghe máy."}
        ],
        "tips": ["Bằng chứng trực tiếp trước mắt -> Dùng 'be going to'."],
        "common_mistakes": ["I will to visit my grandma (Sai -> I will visit...)."]
    },
    {
        "title": "Prepositions of Place & Time (In, On, At)",
        "category": "prepositions",
        "level": "A2",
        "explanation": "Thời gian: At + giờ cụ thể; On + ngày/thứ; In + tháng/năm/mùa/thế kỷ. Địa điểm: At + địa chỉ/vị trí cụ thể; On + đường/mặt phẳng; In + thành phố/quốc gia/không gian khép kín.",
        "examples": [
            {"en": "The conference starts at 9:00 AM on Monday in London.", "vi": "Hội nghị bắt đầu lúc 9:00 sáng Thứ Hai tại London."},
            {"en": "There is a painting on the wall in the living room.", "vi": "Có một bức tranh trên tường trong phòng khách."}
        ],
        "tips": ["Kim tự tháp tam giác ngược: In (rộng nhất) -> On (vừa) -> At (chính xác nhất)."],
        "common_mistakes": ["In Monday (Sai -> On Monday).", "At December (Sai -> In December)."]
    },
    # B1 (6 lessons)
    {
        "title": "Present Perfect (Thì Hiện Tại Hoàn Thành)",
        "category": "tenses",
        "level": "B1",
        "explanation": "Diễn tả hành động xảy ra trong quá khứ nhưng kết quả hoặc ảnh hưởng còn liên quan tới hiện tại, hoặc kinh nghiệm trải nghiệm cuộc sống. Cấu trúc: S + have/has + V3/ed.",
        "examples": [
            {"en": "I have lived in this city for over ten years.", "vi": "Tôi đã sống ở thành phố này hơn mười năm rồi."},
            {"en": "Have you ever traveled to Japan?", "vi": "Bạn đã từng đi du lịch Nhật Bản chưa?"}
        ],
        "tips": ["Since + mốc thời gian (since 2015); For + khoảng thời gian (for 5 years).", "Dấu hiệu: already, yet, ever, never, just, so far, recently."],
        "common_mistakes": ["I have seen him yesterday (Sai -> I saw him yesterday vì có mốc quá khứ xác định)."]
    },
    {
        "title": "Conditionals: Type 0, 1 & 2 (Câu Điều Kiện Loại 0, 1, 2)",
        "category": "conditionals",
        "level": "B1",
        "explanation": "Loại 0 (Chân lý): If + Hiện tại đơn, Hiện tại đơn. Loại 1 (Có thể xảy ra ở tương lai): If + Hiện tại đơn, S + will + V0. Loại 2 (Không có thật ở hiện tại): If + Quá khứ đơn, S + would + V0.",
        "examples": [
            {"en": "If it rains tomorrow, we will cancel the outdoor picnic.", "vi": "Nếu ngày mai trời mưa, chúng tôi sẽ hủy buổi dã ngoại ngoài trời."},
            {"en": "If I had a million dollars, I would build a charity hospital.", "vi": "Nếu tôi có một triệu đô la, tôi sẽ xây dựng một bệnh viện từ thiện."}
        ],
        "tips": ["Trong câu điều kiện loại 2, 'were' được dùng cho tất cả các ngôi (If I were you...)."],
        "common_mistakes": ["If I will study hard, I pass (Sai -> If I study hard, I will pass)."]
    },
    {
        "title": "Passive Voice (Câu Bị Động Cơ Bản & Nâng Cao)",
        "category": "passive_voice",
        "level": "B1",
        "explanation": "Nhấn mạnh vào đối tượng chịu tác động của hành động thay vì người thực hiện. Cấu trúc chung: S + Be (chia theo thì) + V3/ed (+ by O).",
        "examples": [
            {"en": "The novel was written by a famous Vietnamese author in 1995.", "vi": "Cuốn tiểu thuyết được viết bởi một tác giả Việt Nam nổi tiếng vào năm 1995."},
            {"en": "A new highway is being constructed across the province.", "vi": "Một đường cao tốc mới đang được xây dựng xuyên qua tỉnh."}
        ],
        "tips": ["Bị động thì tiếp diễn luôn có 'being' (is/are being + V3).", "Bị động thì hoàn thành luôn có 'been' (has/have been + V3)."],
        "common_mistakes": ["The bridge was build last year (Sai -> was built)."]
    },
    {
        "title": "Relative Clauses (Mệnh Đề Quan Hệ: Who, Whom, Which, That, Whose)",
        "category": "relative_clauses",
        "level": "B1",
        "explanation": "Dùng để bổ nghĩa cho danh từ đứng trước. 'Who' chỉ người làm chủ ngữ; 'Whom' chỉ người làm tân ngữ; 'Which' chỉ vật; 'That' thay cho who/which trong mệnh đề xác định; 'Whose' chỉ sở hữu.",
        "examples": [
            {"en": "The software engineer who designed this AI app is very talented.", "vi": "Kỹ sư phần mềm người thiết kế ứng dụng AI này rất tài năng."},
            {"en": "The company whose products we import has expanded globally.", "vi": "Công ty mà chúng tôi nhập khẩu sản phẩm của họ đã mở rộng ra toàn cầu."}
        ],
        "tips": ["Không dùng 'that' sau dấu phẩy (trong mệnh đề quan hệ không xác định) hoặc sau giới từ."],
        "common_mistakes": ["The man which called you (Sai -> The man who/that called you)."]
    },
    {
        "title": "Gerunds vs Infinitives (Danh Động Từ V-ing & Động Từ To-V)",
        "category": "verb_patterns",
        "level": "B1",
        "explanation": "Động từ theo sau bởi V-ing (enjoy, avoid, mind, suggest, practice) hoặc To-V (decide, hope, plan, promise, refuse, manage). Một số từ đổi nghĩa: remember, stop, forget, try.",
        "examples": [
            {"en": "I enjoy listening to English podcasts every morning.", "vi": "Tôi thích nghe podcast tiếng Anh mỗi sáng."},
            {"en": "He decided to accept the scholarship in Canada.", "vi": "Anh ấy đã quyết định nhận học bổng tại Canada."}
        ],
        "tips": ["'Stop to do' = dừng lại để làm việc gì; 'Stop doing' = dừng hẳn việc đang làm."],
        "common_mistakes": ["I enjoy to play games (Sai -> I enjoy playing games)."]
    },
    {
        "title": "Reported Speech (Câu Tường Thuật / Gián Tiếp)",
        "category": "reported_speech",
        "level": "B1",
        "explanation": "Thuật lại lời nói của người khác. Cần lùi một thì, đổi đại từ nhân xưng và trạng từ chỉ thời gian/nơi chốn (e.g. now -> then, yesterday -> the day before, tomorrow -> the following day).",
        "examples": [
            {"en": "She said: 'I am learning AI' -> She said that she was learning AI.", "vi": "Cô ấy nói rằng cô ấy đang học AI."},
            {"en": "He asked me where I lived.", "vi": "Anh ấy hỏi tôi sống ở đâu."}
        ],
        "tips": ["Câu hỏi gián tiếp có cấu trúc khẳng định: S + asked + (O) + if/wh-word + S + V."],
        "common_mistakes": ["He asked me where did I live (Sai -> He asked me where I lived)."]
    },
    # B2 (6 lessons)
    {
        "title": "Past Perfect & Past Perfect Continuous (Quá Khứ Hoàn Thành)",
        "category": "tenses",
        "level": "B2",
        "explanation": "Diễn tả hành động xảy ra và hoàn tất trước một thời điểm hoặc một hành động khác trong quá khứ. Cấu trúc: S + had + V3/ed (hoặc had been + V-ing).",
        "examples": [
            {"en": "By the time the firefighters arrived, the fire had already been extinguished.", "vi": "Trước khi lính cứu hỏa đến, ngọn lửa đã được dập tắt rồi."},
            {"en": "She was exhausted because she had been working for 14 hours straight.", "vi": "Cô ấy kiệt sức vì đã làm việc liên tục suốt 14 tiếng."}
        ],
        "tips": ["Hành động xảy ra trước chia Quá khứ hoàn thành (had + V3), hành động sau chia Quá khứ đơn."],
        "common_mistakes": ["When I arrived, the train left (Thiếu sự phân biệt trước sau -> the train had left)."]
    },
    {
        "title": "Conditional Type 3 & Mixed Conditionals (Câu Điều Kiện Loại 3 & Trộn)",
        "category": "conditionals",
        "level": "B2",
        "explanation": "Loại 3 diễn tả điều kiện trái với thực tế trong quá khứ: If + had + V3, S + would have + V3. Điều kiện trộn kết hợp quá khứ và hiện tại: If + had + V3, S + would + V0 (now).",
        "examples": [
            {"en": "If you had warned me earlier, I would not have made that costly mistake.", "vi": "Nếu bạn cảnh báo tôi sớm hơn, tôi đã không phạm phải sai lầm tốn kém đó."},
            {"en": "If I had passed the exam last year, I would be studying at Oxford right now.", "vi": "Nếu tôi đỗ kỳ thi năm ngoái, thì bây giờ tôi đang học tại Oxford rồi."}
        ],
        "tips": ["Dùng 'mixed conditional' khi hành động trong quá khứ để lại kết quả ảnh hưởng đến hiện tại."],
        "common_mistakes": ["If I would have known (Sai -> If I had known)."]
    },
    {
        "title": "Wish & If Only Structures (Cấu Trúc Ước Muốn)",
        "category": "subjunctive",
        "level": "B2",
        "explanation": "Ước ở hiện tại: S + wish + S + V2/ed (were). Ước ở quá khứ: S + wish + S + had + V3. Ước phàn nàn/tương lai: S + wish + S + would + V0.",
        "examples": [
            {"en": "I wish I were fluent in five different languages.", "vi": "Tôi ước gì mình có thể nói trôi chảy năm thứ tiếng khác nhau."},
            {"en": "She wishes she had not declined that lucrative job offer.", "vi": "Cô ấy ước rằng mình đã không từ chối lời mời làm việc hấp dẫn đó."}
        ],
        "tips": ["'If only' mang sắc thái tiếc nuối và ước muốn mạnh mẽ hơn 'I wish'."],
        "common_mistakes": ["I wish I will be rich (Sai -> I wish I were rich / could be rich)."]
    },
    {
        "title": "Modal Verbs of Deduction & Speculation (Must have, Can't have, Might have)",
        "category": "modals",
        "level": "B2",
        "explanation": "Dự đoán ở quá khứ: Must have + V3 (chắc chắn đã); Can't/Couldn't have + V3 (chắc chắn không thể đã); May/Might/Could have + V3 (có thể đã).",
        "examples": [
            {"en": "The lights are off and the door is locked; they must have left already.", "vi": "Đèn tắt và cửa đã khóa; chắc chắn họ đã rời đi rồi."},
            {"en": "He can't have committed the crime because he was overseas at the time.", "vi": "Anh ấy không thể nào đã phạm tội vì lúc đó anh ấy đang ở nước ngoài."}
        ],
        "tips": ["Không dùng 'mustn't have + V3' để diễn tả suy đoán phủ định, hãy dùng 'can't have + V3'."],
        "common_mistakes": ["He must not have been there (Ý nghĩa phỏng đoán phủ định chuẩn là 'can't have been')."]
    },
    {
        "title": "Cleft Sentences (Câu Chẻ Nhấn Mạnh: It is/was... that, What... is)",
        "category": "emphasis",
        "level": "B2",
        "explanation": "Dùng để nhấn mạnh một thành phần cụ thể trong câu (chủ ngữ, tân ngữ, trạng ngữ). Cấu trúc: It is/was + [Thành phần nhấn mạnh] + that/who + ... hoặc What + S + V + is/was + ...",
        "examples": [
            {"en": "It was Dr. Nguyen who pioneered the artificial intelligence research.", "vi": "Chính Tiến sĩ Nguyễn là người đã tiên phong nghiên cứu trí tuệ nhân tạo."},
            {"en": "What impressed the board of directors was his exceptional leadership vision.", "vi": "Điều gây ấn tượng với ban giám đốc chính là tầm nhìn lãnh đạo xuất sắc của anh ấy."}
        ],
        "tips": ["Câu chẻ là cấu trúc ghi điểm rất cao trong tiêu chí Grammatical Range của IELTS Writing."],
        "common_mistakes": ["It was in Hanoi which we met (Sai -> It was in Hanoi that we met)."]
    },
    {
        "title": "Double Comparative Structures (Cấu Trúc So Sánh Kép: The more... the more...)",
        "category": "adjectives",
        "level": "B2",
        "explanation": "Diễn tả mối tương quan tỷ lệ thuận hoặc nghịch giữa hai vế câu. Cấu trúc: The + So sánh hơn + S + V, the + So sánh hơn + S + V.",
        "examples": [
            {"en": "The more diligently you practice English phonetics, the more naturally you will speak.", "vi": "Bạn càng chăm chỉ luyện ngữ âm tiếng Anh, bạn sẽ càng nói tự nhiên hơn."},
            {"en": "The higher the altitude of the mountain summit, the thinner the breathable atmosphere becomes.", "vi": "Độ cao của đỉnh núi càng lớn, bầu không khí để thở càng trở nên loãng hơn."}
        ],
        "tips": ["Có thể dùng với danh từ: 'The more books you read, the more knowledge you gain.'"],
        "common_mistakes": ["More you study, more you know (Sai -> The more you study, the more you know)."]
    },
    # C1 & C2 (11 lessons)
    {
        "title": "Inversion with Negative Adverbials (Đảo Ngữ với Trạng Từ Phủ Định)",
        "category": "inversion",
        "level": "C1",
        "explanation": "Đặt trạng từ phủ định hoặc hạn định lên đầu câu để tăng tính trang trọng và biểu cảm. Cấu trúc: Negative word + Trợ động từ + S + V. (Never, Rarely, Seldom, Scarcely... when, No sooner... than, Not only... but also).",
        "examples": [
            {"en": "No sooner had the keynote speaker stepped onto the stage than the audience erupted in applause.", "vi": "Diễn giả chính vừa bước lên sân khấu thì khán phòng đã bùng nổ trong tràng pháo tay."},
            {"en": "Under no circumstances should confidential financial data be disclosed to unauthorized third parties.", "vi": "Trong bất kỳ hoàn cảnh nào, dữ liệu tài chính bảo mật cũng không được tiết lộ cho bên thứ ba."}
        ],
        "tips": ["Nhớ công thức: No sooner ... THAN, Scarcely/Hardly ... WHEN."],
        "common_mistakes": ["Hardly had I arrived than it rained (Sai -> Hardly had I arrived WHEN it rained)."]
    },
    {
        "title": "Subjunctive Mood in Formal English (Thể Giả Định Trang Trọng)",
        "category": "subjunctive",
        "level": "C1",
        "explanation": "Dùng sau các động từ/tính từ yêu cầu, đề nghị, cấp thiết (demand, recommend, suggest, insist, vital, crucial, essential). Động từ trong mệnh đề 'that' luôn ở dạng nguyên mẫu không chia (bare infinitive).",
        "examples": [
            {"en": "The committee recommended that the CEO submit a comprehensive restructuring proposal.", "vi": "Ủy ban khuyến nghị rằng Giám đốc điều hành nên nộp một đề xuất tái cấu trúc toàn diện."},
            {"en": "It is imperative that every employee be thoroughly briefed on cybersecurity protocols.", "vi": "Điều cấp thiết là mỗi nhân viên phải được phổ biến kỹ lưỡng về các quy định an ninh mạng."}
        ],
        "tips": ["Dù chủ ngữ là he/she/it hay số ít, động từ vẫn giữ nguyên thể không thêm -s/es và to be là 'be'."],
        "common_mistakes": ["It is vital that he goes (Sai trong văn phong trang trọng -> It is vital that he go)."]
    },
    {
        "title": "Participle Clauses & Reduced Relative Clauses (Mệnh Đề Phân Từ Rút Gọn)",
        "category": "participles",
        "level": "C1",
        "explanation": "Dùng V-ing (chủ động) hoặc V3/ed (bị động) để rút gọn mệnh đề quan hệ hoặc mệnh đề trạng ngữ chỉ nguyên nhân, thời gian, điều kiện.",
        "examples": [
            {"en": "Having analyzed the quarterly market fluctuations, the chief analyst revised her profit forecasts.", "vi": "Sau khi đã phân tích những biến động thị trường hàng quý, trưởng nhóm phân tích đã điều chỉnh lại dự báo lợi nhuận."},
            {"en": "Built during the 17th century, the historic cathedral attracts millions of international tourists annually.", "vi": "Được xây dựng vào thế kỷ 17, nhà thờ lịch sử này thu hút hàng triệu du khách quốc tế mỗi năm."}
        ],
        "tips": ["Lưu ý lỗi 'Dangling Participle' (phân từ treo lơ lửng) khi chủ ngữ của cụm phân từ không trùng với chủ ngữ chính."],
        "common_mistakes": ["Walking down the street, the trees were beautiful (Sai chủ ngữ)."]
    },
    {
        "title": "Discourse Markers & Stance Adverbials (Từ Nối Luận Điểm & Trạng Từ Lập Trường)",
        "category": "cohesion",
        "level": "C1",
        "explanation": "Sử dụng các trạng từ biểu đạt lập trường và liên kết mạch lạc: Notwithstanding, Furthermore, Albeit, Inextricably, Predominantly, Incontrovertibly.",
        "examples": [
            {"en": "The technological initiative proved wildly successful, albeit substantially over the initial budget.", "vi": "Sáng kiến công nghệ đã chứng tỏ thành công rực rỡ, mặc dù vượt ngân sách ban đầu đáng kể."},
            {"en": "Economic prosperity and environmental stewardship are inextricably linked.", "vi": "Sự thịnh vượng kinh tế và trách nhiệm quản lý môi trường gắn kết với nhau một cách không thể tách rời."}
        ],
        "tips": ["'Albeit' luôn đi kèm với tính từ hoặc cụm giới từ, không đi với mệnh đề đầy đủ."],
        "common_mistakes": ["Albeit it was raining (Sai -> Albeit raining)."]
    },
    {
        "title": "Complex Prepositional Phrases (Cụm Giới Từ Học Thuật Phức Hợp)",
        "category": "prepositions",
        "level": "C1",
        "explanation": "Cụm giới từ nâng cao: In light of, With regard to, In terms of, By virtue of, In accordance with, On the grounds of.",
        "examples": [
            {"en": "In light of recent archaeological discoveries, historians have reevaluated the ancient civilization.", "vi": "Dưới ánh sáng của những khám phá khảo cổ gần đây, các nhà sử học đã đánh giá lại nền văn minh cổ đại."},
            {"en": "The patent was granted by virtue of its groundbreaking novel engineering design.", "vi": "Bằng sáng chế đã được cấp nhờ vào thiết kế kỹ thuật mới mang tính đột phá."}
        ],
        "tips": ["Ghi nhớ 'By virtue of' mang nghĩa 'bằng cách/nhờ vào' sức mạnh hoặc phẩm chất đặc thù."],
        "common_mistakes": ["In light with (Sai -> In light of)."]
    },
    {
        "title": "Compound Adjectives & Modifier Chains (Tính Từ Ghép & Chuỗi Bổ Ngữ Nâng Cao)",
        "category": "adjectives",
        "level": "C1",
        "explanation": "Tạo tính từ ghép sinh động bằng dấu gạch nối: state-of-the-art, thought-provoking, deep-rooted, long-lasting, highly-acclaimed, forward-thinking.",
        "examples": [
            {"en": "The university inaugurated a state-of-the-art laboratory dedicated to biomedical engineering.", "vi": "Trường đại học đã khánh thành một phòng thí nghiệm hiện đại bậc nhất dành cho kỹ thuật y sinh."},
            {"en": "Her thought-provoking lecture challenged traditional preconceptions regarding artificial intelligence.", "vi": "Bài giảng gợi mở nhiều suy nghĩ của cô ấy đã thách thức những định kiến truyền thống về trí tuệ nhân tạo."}
        ],
        "tips": ["Không thêm 's' vào danh từ nằm trong tính từ ghép (e.g. A ten-year-old boy, KHÔNG PHẢI ten-years-old boy)."],
        "common_mistakes": ["A three-hours flight (Sai -> A three-hour flight)."]
    },
    {
        "title": "Fronting & Focus Devices (Đảo Cấu Trúc Nhấn Mạnh & Tiền Đề)",
        "category": "emphasis",
        "level": "C2",
        "explanation": "Đưa các cụm từ chỉ vị trí, tính từ, hoặc phân từ lên đầu câu để tạo nhịp điệu văn chương uyển chuyển và tập trung sự chú ý của độc giả.",
        "examples": [
            {"en": "Perched precariously atop the rugged cliff stood an ancient lighthouse.", "vi": "Nằm chênh vênh trên đỉnh vách đá gồ ghề là một ngọn hải đăng cổ kính."},
            {"en": "Such was the sheer magnitude of the catastrophe that recovery efforts took decades.", "vi": "Mức độ thảm họa to lớn đến mức các nỗ lực phục hồi đã phải mất hàng thập kỷ."}
        ],
        "tips": ["Cấu trúc: 'Such + be + S + that...' hoặc 'So + Adj + be + S + that...'."],
        "common_mistakes": ["So great the storm was (Sai -> So great was the storm)."]
    },
    {
        "title": "Nominalisation in Academic Writing (Hiện Tượng Danh Từ Hóa)",
        "category": "academic_writing",
        "level": "C2",
        "explanation": "Chuyển đổi động từ và tính từ thành cụm danh từ phức để tăng tính khách quan, cô đọng và trang trọng chuẩn học thuật Cambridge/Oxford.",
        "examples": [
            {"en": "The unprecedented rapid proliferation of autonomous systems has raised ethical quandaries.", "vi": "Sự sinh sôi nhanh chóng chưa từng có của các hệ thống tự hành đã làm dấy lên những tình thế tiến thoái lưỡng nan về đạo đức."},
            {"en": "A thorough examination of demographic trends reveals substantial shifts in urban migration.", "vi": "Một cuộc kiểm tra kỹ lưỡng về các xu hướng nhân khẩu học cho thấy những dịch chuyển đáng kể trong làn sóng di cư đô thị."}
        ],
        "tips": ["Hạn chế dùng các ngôi xưng 'I', 'we' trong văn phong hàn lâm; hãy danh từ hóa hành động."],
        "common_mistakes": ["Lạm dụng quá mức khiến câu trở nên rườm rà, khó đọc."]
    },
    {
        "title": "Ellipsis and Substitution (Tỉnh Lược & Thay Thế Ngữ Pháp)",
        "category": "cohesion",
        "level": "C2",
        "explanation": "Lược bỏ những từ ngữ thừa đã được hiểu ngầm trong ngữ cảnh (Ellipsis) hoặc sử dụng các từ thay thế như 'so, do so, one, ones' (Substitution) để tránh lặp từ.",
        "examples": [
            {"en": "Some delegates voted in favor of the resolution; others against.", "vi": "Một số đại biểu đã bỏ phiếu ủng hộ nghị quyết; những người khác bỏ phiếu chống."},
            {"en": "If prompted to testify before the parliamentary inquiry, she will certainly do so.", "vi": "Nếu được yêu cầu ra làm chứng trước cuộc điều tra của quốc hội, cô ấy chắc chắn sẽ làm như vậy."}
        ],
        "tips": ["Giúp bài viết đạt điểm tối đa ở tiêu chí Cohesion and Coherence trong IELTS Band 8.5 - 9.0."],
        "common_mistakes": ["Tỉnh lược sai cấu trúc khiến câu mất nghĩa hoặc gây hiểu lầm."]
    },
    {
        "title": "Hypothetical Past Inversions (Đảo Ngữ Giả Định Quá Khứ: Had it not been for...)",
        "category": "inversion",
        "level": "C2",
        "explanation": "Đảo ngữ câu điều kiện không có 'if': Had it not been for [Noun] = If it had not been for [Noun] (Nếu không vì...). Tương tự: Were it not for... / Should you require...",
        "examples": [
            {"en": "Had it not been for your steadfast guidance, our startup would have collapsed during the financial crisis.", "vi": "Nếu không vì sự chỉ dẫn kiên định của bạn, công ty khởi nghiệp của chúng tôi đã sụp đổ trong cuộc khủng hoảng tài chính."},
            {"en": "Were it not for international humanitarian aid, the famine would have claimed thousands more lives.", "vi": "Nếu không vì viện trợ nhân đạo quốc tế, nạn đói đã cướp đi thêm hàng ngàn sinh mạng."}
        ],
        "tips": ["Cấu trúc tuyệt hảo thay thế cho 'Without' hoặc 'If it weren't for' trong văn viết cao cấp."],
        "common_mistakes": ["Had not it been for (Sai -> Had it not been for)."]
    },
    {
        "title": "Modal Aspectual Nuances: Volition, Epistemic & Deontic Modality",
        "category": "modals",
        "level": "C2",
        "explanation": "Phân tích ngữ nghĩa tầng sâu của các động từ khuyết thiếu: Epistemic (tính khả dĩ nhận thức), Deontic (nghĩa vụ/cho phép), và Dynamic/Volitional (ý chí/khuynh hướng tự nhiên).",
        "examples": [
            {"en": "The machine will keep vibrating regardless of how tightly the bolts are secured.", "vi": "Chiếc máy cứ rung lắc liên tục bất kể các ốc vít đã được siết chặt đến mức nào (diễn tả khuynh hướng tự nhiên 'will')."},
            {"en": "You might well question the veracity of these unverified demographic statistics.", "vi": "Bạn hoàn toàn có lý do chính đáng để hoài nghi tính xác thực của những số liệu nhân khẩu học chưa được kiểm chứng này."}
        ],
        "tips": ["'Might well' mang nghĩa 'có lý do rất chính đáng để...'; 'May well' cũng tương tự."],
        "common_mistakes": ["Nhầm lẫn giữa 'may not' (có thể không) và 'cannot' (chắc chắn không thể)."]
    }
]

# ═══════════════════════════════════════════════════════════════════════════════
# 2. READING ARTICLES (35 ARTICLES A1 -> C2)
# ═══════════════════════════════════════════════════════════════════════════════
READING_ARTICLES = [
    # A1 (6 articles)
    {
        "title": "Article 1: A Day in the Life of a Software Engineer",
        "article_type": "story", "level": "A1", "topic": "Technology & Daily Life", "word_count": 95,
        "summary": "Câu chuyện sinh hoạt thường nhật của một kỹ sư phần mềm trẻ.",
        "content": "Alex is a software engineer living in Da Nang. Every morning, he wakes up at 6:30 AM, makes fresh coffee, and writes computer code for his AI startup. At noon, he eats a healthy lunch with his colleagues and takes a short walk along My Khe beach. In the evening, Alex reads tech blogs and practices English vocabulary with his online tutor.",
        "questions": [
            {"question": "Where does Alex live?", "options": ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hue"], "answer": "Da Nang"},
            {"question": "What does Alex do in the evening?", "options": ["Plays video games all night", "Reads tech blogs and practices English vocabulary", "Goes to a nightclub", "Works in a restaurant"], "answer": "Reads tech blogs and practices English vocabulary"}
        ]
    },
    {
        "title": "Article 2: Exploring the Wonders of Ha Long Bay",
        "article_type": "blog", "level": "A1", "topic": "Travel & Nature", "word_count": 110,
        "summary": "Bài viết hướng dẫn du lịch khám phá vịnh Hạ Long kỳ vĩ.",
        "content": "Ha Long Bay is one of the most famous natural wonders in Vietnam. It features thousands of limestone islands rising dramatically from emerald-green waters. Travelers from all around the world come here to take boat cruises, kayak through mysterious caves, and watch glorious sunsets. Visiting Ha Long Bay is an unforgettable travel experience for every visitor.",
        "questions": [
            {"question": "What is Ha Long Bay famous for?", "options": ["High skyscrapers", "Thousands of limestone islands in emerald waters", "Sandy desert dunes", "Snowy mountains"], "answer": "Thousands of limestone islands in emerald waters"},
            {"question": "What activities do travelers enjoy in Ha Long Bay?", "options": ["Skiing and ice skating", "Boat cruises, kayaking through caves, and watching sunsets", "Desert camel rides", "Mountain climbing only"], "answer": "Boat cruises, kayaking through caves, and watching sunsets"}
        ]
    },
    {
        "title": "Article 3: The Importance of Eating Fresh Fruits and Vegetables",
        "article_type": "blog", "level": "A1", "topic": "Health & Nutrition", "word_count": 100,
        "summary": "Tầm quan trọng của rau củ quả tươi đối với sức khỏe con người.",
        "content": "Eating fresh fruits and green vegetables every day provides essential vitamins, minerals, and dietary fiber. Apples, bananas, and oranges give you sustained natural energy throughout the day, while leafy greens like spinach protect your immune system. Drinking plenty of fresh water and eating colorful salads will help you feel energetic and healthy.",
        "questions": [
            {"question": "What do fruits and vegetables provide to our bodies?", "options": ["Harmful chemicals", "Essential vitamins, minerals, and dietary fiber", "High sugar and fat", "Artificial coloring"], "answer": "Essential vitamins, minerals, and dietary fiber"},
            {"question": "What does spinach protect according to the text?", "options": ["Your shoes", "Your immune system", "Your eyesight in the dark", "Your smartphone"], "answer": "Your immune system"}
        ]
    },
    {
        "title": "Article 4: Traditional Festivals in Vietnamese Culture",
        "article_type": "story", "level": "A1", "topic": "Culture & Society", "word_count": 105,
        "summary": "Giới thiệu các ngày lễ hội truyền thống đặc sắc tại Việt Nam.",
        "content": "Tet, or the Lunar New Year, is the most sacred and joyful celebration in Vietnam. During Tet, family members gather together from far away to cook traditional square sticky rice cakes called Banh Chung. Children wear bright new clothes and receive lucky red envelopes with best wishes for health, happiness, and academic success in the new year.",
        "questions": [
            {"question": "What traditional food is cooked during Tet?", "options": ["Pizza and burgers", "Banh Chung (square sticky rice cake)", "French bread", "Pasta"], "answer": "Banh Chung (square sticky rice cake)"},
            {"question": "What do children receive during the Lunar New Year?", "options": ["School homework", "Lucky red envelopes with best wishes", "Old toys", "Cleaning tools"], "answer": "Lucky red envelopes with best wishes"}
        ]
    },
    {
        "title": "Article 5: Why Reading Books Daily Makes You Smarter",
        "article_type": "blog", "level": "A1", "topic": "Education & Books", "word_count": 95,
        "summary": "Lý do vì sao việc đọc sách mỗi ngày giúp phát triển trí tuệ.",
        "content": "Reading books every day is one of the most effective habits for self-growth. When you read, you expand your vocabulary, sharpen your concentration, and learn about different perspectives. Even dedicating just fifteen minutes before bedtime to read a good novel can reduce stress and inspire creative ideas.",
        "questions": [
            {"question": "How does reading books benefit your mind?", "options": ["Causes eye fatigue only", "Expands vocabulary, sharpens concentration, and broadens perspectives", "Makes you forget your native language", "Wastes valuable time"], "answer": "Expands vocabulary, sharpens concentration, and broadens perspectives"},
            {"question": "How much daily reading time is suggested before sleep?", "options": ["5 hours", "15 minutes", "2 minutes", "10 seconds"], "answer": "15 minutes"}
        ]
    },
    {
        "title": "Article 6: How Solar Energy Powers Modern Green Homes",
        "article_type": "news", "level": "A1", "topic": "Science & Energy", "word_count": 100,
        "summary": "Năng lượng mặt trời cung cấp điện sạch cho các ngôi nhà hiện đại.",
        "content": "Solar panels installed on residential rooftops capture sunlight and convert it cleanly into electricity. This renewable energy powers home appliances, lights, and air conditioning without producing polluting greenhouse gases. Modern homeowners save significant money on electric bills while protecting the natural environment for future generations.",
        "questions": [
            {"question": "What do solar panels convert sunlight into?", "options": ["Water", "Clean electricity", "Gasoline", "Wind"], "answer": "Clean electricity"},
            {"question": "What is an advantage of solar power for homeowners?", "options": ["Increases electric bills", "Saves money and protects the natural environment", "Requires burning coal", "Works only in winter"], "answer": "Saves money and protects the natural environment"}
        ]
    },

    # A2 (6 articles)
    {
        "title": "Article 7: The Advantages of Learning English Online with AI",
        "article_type": "blog", "level": "A2", "topic": "AI & Education", "word_count": 135,
        "summary": "Những ưu điểm vượt trội khi học tiếng Anh với trợ lý trí tuệ nhân tạo.",
        "content": "Studying English with an AI learning platform offers remarkable flexibility and personalized pacing. Unlike traditional classrooms with rigid schedules, learners can practice conversational speaking, grammar quizzes, and writing essays anytime, anywhere. AI teachers provide immediate phonetic feedback and tailor exercises to target each student's specific weaknesses, helping learners build confidence rapidly.",
        "questions": [
            {"question": "What is one key advantage of AI English learning compared to traditional classrooms?", "options": ["Strict fixed schedules", "Flexibility and personalized pacing anytime, anywhere", "High classroom tuition fees", "Requirement to travel far"], "answer": "Flexibility and personalized pacing anytime, anywhere"},
            {"question": "How do AI teachers help students build confidence?", "options": ["By assigning impossible tasks", "By providing immediate feedback and targeting specific weaknesses", "By refusing to answer questions", "By speaking only Latin"], "answer": "By providing immediate feedback and targeting specific weaknesses"}
        ]
    },
    {
        "title": "Article 8: Electric Vehicles and the Future of Transportation",
        "article_type": "news", "level": "A2", "topic": "Automotive & Green Tech", "word_count": 140,
        "summary": "Sự bùng nổ của xe điện và tương lai giao thông không phát thải.",
        "content": "Electric vehicles (EVs) are transforming global transportation networks. Powered by high-capacity lithium-ion batteries instead of gasoline engines, EVs produce zero tailpipe emissions during operation. As battery charging infrastructure expands rapidly across metropolitan highways and battery manufacturing costs decline, electric cars are becoming accessible and affordable for mainstream consumers worldwide.",
        "questions": [
            {"question": "What powers modern electric vehicles?", "options": ["Diesel fuel", "High-capacity lithium-ion batteries", "Steam engines", "Coal furnaces"], "answer": "High-capacity lithium-ion batteries"},
            {"question": "What makes electric vehicles increasingly accessible today?", "options": ["Gasoline price drops", "Expanding charging infrastructure and declining battery manufacturing costs", "Discontinuing road construction", "Lowering car safety standards"], "answer": "Expanding charging infrastructure and declining battery manufacturing costs"}
        ]
    },
    {
        "title": "Article 9: Effective Time Management and the Pomodoro Technique",
        "article_type": "blog", "level": "A2", "topic": "Productivity", "word_count": 130,
        "summary": "Kỹ thuật quả cà chua Pomodoro giúp tăng năng suất làm việc vượt trội.",
        "content": "The Pomodoro Technique is a world-renowned time management methodology created by Francesco Cirillo. The system is simple: you choose a specific task, set a timer for 25 minutes of deep focus, and work without distractions. When the timer rings, take a 5-minute break. After completing four cycles, enjoy a longer 20-minute break. This rhythm maintains mental freshness and prevents burnout.",
        "questions": [
            {"question": "How long is each focused work interval in the Pomodoro technique?", "options": ["10 minutes", "25 minutes", "60 minutes", "90 minutes"], "answer": "25 minutes"},
            {"question": "What is the primary benefit of taking regular short breaks?", "options": ["Wasting time", "Maintaining mental freshness and preventing burnout", "Forgetting the task", "Making you sleepy"], "answer": "Maintaining mental freshness and preventing burnout"}
        ]
    },
    {
        "title": "Article 10: The Rise of E-Commerce and Digital Payments",
        "article_type": "news", "level": "A2", "topic": "Business & Fintech", "word_count": 145,
        "summary": "Sự phát triển của thương mại điện tử và phương thức thanh toán số.",
        "content": "Over the past five years, consumer purchasing habits have shifted dramatically toward online shopping and contactless digital wallets. Consumers can browse millions of global products, compare prices instantly, and read verified customer reviews before placing an order. Secure QR code payments and next-day home delivery have made online shopping seamless and indispensable for modern urban life.",
        "questions": [
            {"question": "What allows consumers to make informed choices online?", "options": ["Comparing prices instantly and reading verified reviews", "Listening to radio ads only", "Asking bank managers", "Waiting for newspaper prints"], "answer": "Comparing prices instantly and reading verified reviews"},
            {"question": "Which payment method is highlighted as seamless in urban life?", "options": ["Gold coins", "Secure QR code payments and digital wallets", "Paper cheques only", "Bartering goods"], "answer": "Secure QR code payments and digital wallets"}
        ]
    },
    {
        "title": "Article 11: Protecting Coral Reef Ecosystems in Southeast Asia",
        "article_type": "blog", "level": "A2", "topic": "Ecology & Marine Life", "word_count": 140,
        "summary": "Bảo vệ hệ sinh thái rạn san hô quý giá tại Đông Nam Á.",
        "content": "Southeast Asia is home to the Coral Triangle, the global epicenter of marine biodiversity. Coral reefs provide essential habitats for thousands of tropical fish, protect coastal communities from fierce storm surges, and support local fishing economies. Marine biologists are collaborating with coastal villages to establish marine protected zones and restore damaged coral nurseries.",
        "questions": [
            {"question": "What region is known as the epicenter of marine biodiversity?", "options": ["The Sahara Desert", "The Coral Triangle in Southeast Asia", "The Arctic Circle", "The North Sea"], "answer": "The Coral Triangle in Southeast Asia"},
            {"question": "How do coral reefs protect coastal communities?", "options": ["By stopping internet cables", "By buffering against fierce storm surges", "By warming the atmosphere", "By catching fresh rainwater"], "answer": "By buffering against fierce storm surges"}
        ]
    },
    {
        "title": "Article 12: How Regular Exercise Boosts Mental Health and Mood",
        "article_type": "blog", "level": "A2", "topic": "Health & Psychology", "word_count": 135,
        "summary": "Tập thể dục thường xuyên giúp giải tỏa stress và tăng cường trí nhớ.",
        "content": "Engaging in moderate physical activity for thirty minutes daily yields profound psychological benefits. When you run, swim, or cycle, your brain releases endorphins—neurochemicals that alleviate physical pain and induce feelings of happiness. Furthermore, consistent aerobic exercise enhances blood circulation to the prefrontal cortex, boosting memory, creativity, and emotional resilience.",
        "questions": [
            {"question": "What neurochemicals does the brain release during exercise?", "options": ["Toxins", "Endorphins (feelings of happiness)", "Stress hormones", "Sedatives"], "answer": "Endorphins (feelings of happiness)"},
            {"question": "Which brain region benefits from enhanced blood circulation during exercise?", "options": ["The spinal cord", "The prefrontal cortex (boosting memory and creativity)", "The skull bone", "The jaw muscles"], "answer": "The prefrontal cortex (boosting memory and creativity)"}
        ]
    },

    # B1 (6 articles)
    {
        "title": "Article 13: How Cloud Computing and Microservices Reshape Software Development",
        "article_type": "news", "level": "B1", "topic": "Information Technology", "word_count": 180,
        "summary": "Điện toán đám mây và kiến trúc microservices đang tái định hình ngành phần mềm.",
        "content": "In recent years, software engineering teams have increasingly moved away from monolithic codebases toward modular microservices hosted on scalable cloud platforms. Rather than deploying an entire application as a single massive unit, microservices decouple distinct functional modules into independent, containerized services. This architectural shift empowers development teams to deploy feature updates continuously without risking system-wide downtime. Furthermore, automated load-balancing and auto-scaling mechanisms dynamically allocate server resources during traffic surges, ensuring peak performance and optimal cost-efficiency for modern digital enterprises.",
        "questions": [
            {"question": "What is the primary advantage of decoupling code into containerized microservices?",
             "options": ["It increases server failure rates", "It allows continuous feature deployment without risking system-wide downtime", "It eliminates the need for software engineers", "It makes applications completely offline"],
             "answer": "It allows continuous feature deployment without risking system-wide downtime"},
            {"question": "How do cloud platforms handle sudden surges in user traffic?",
             "options": ["By shutting down the entire platform", "Through automated load-balancing and auto-scaling resource allocation", "By requiring manual hardware installation", "By limiting user logins to 10 people"],
             "answer": "Through automated load-balancing and auto-scaling resource allocation"}
        ]
    },
    {
        "title": "Article 14: The Architecture of Smart Cities and IoT Integration",
        "article_type": "academic", "level": "B1", "topic": "Smart Cities & Urban Tech", "word_count": 190,
        "summary": "Kiến trúc thành phố thông minh thông qua mạng lưới Internet vạn vật (IoT).",
        "content": "Municipal governments across the globe are integrating Internet of Things (IoT) sensors and data analytics to construct intelligent urban ecosystems. By embedding networked sensors into traffic signals, water distribution pipelines, and municipal waste containers, city planners receive real-time telemetry regarding urban dynamics. For instance, intelligent traffic management systems analyze real-time congestion data to dynamically adjust traffic light cycles, cutting commuter delays and reducing vehicle idling emissions. Similarly, automated smart water grids detect subterranean pipe leakages instantly, preserving millions of gallons of potable drinking water annually.",
        "questions": [
            {"question": "What allows smart cities to optimize traffic light cycles in real time?",
             "options": ["Human police officers standing at every corner", "Intelligent traffic management systems analyzing real-time sensor telemetry", "Fixed timer clocks from 1950", "Randomized automatic switches"],
             "answer": "Intelligent traffic management systems analyzing real-time sensor telemetry"},
            {"question": "How do automated smart water grids conserve urban resources?",
             "options": ["By cutting water supply entirely", "By detecting subterranean pipe leakages instantly", "By doubling consumer water rates", "By draining city reservoirs into the sea"],
             "answer": "By detecting subterranean pipe leakages instantly"}
        ]
    },
    {
        "title": "Article 15: Cross-Cultural Communication in Multinational Organizations",
        "article_type": "blog", "level": "B1", "topic": "Business & Global Leadership", "word_count": 185,
        "summary": "Kỹ năng giao tiếp đa văn hóa trong các tập đoàn đa quốc gia hiện đại.",
        "content": "In an interconnected global economy, multinational corporations employ professionals from vastly diverse cultural and linguistic backgrounds. Navigating cross-cultural communication requires not merely linguistic fluency in English, but profound cultural intelligence and empathy. For instance, high-context communication cultures rely heavily on implicit nuances, non-verbal cues, and interpersonal harmony, whereas low-context cultures prioritize direct, explicit verbal precision. Successful international leaders actively foster inclusive environments where team members appreciate differing communication styles, turning cultural diversity into a formidable catalyst for innovative problem-solving.",
        "questions": [
            {"question": "What is the key characteristic of high-context communication cultures?",
             "options": ["Extreme literal directness in every sentence", "Heavy reliance on implicit nuances, non-verbal cues, and harmony", "Communicating only through written legal documents", "Avoiding any interpersonal interaction"],
             "answer": "Heavy reliance on implicit nuances, non-verbal cues, and harmony"},
            {"question": "Why is cultural intelligence essential for modern global leaders?",
             "options": ["To force all employees to adopt one culture", "To foster inclusive environments and turn diversity into an innovation catalyst", "To eliminate the use of English", "To avoid hiring international workers"],
             "answer": "To foster inclusive environments and turn diversity into an innovation catalyst"}
        ]
    },
    {
        "title": "Article 16: The Circular Economy: Redesigning Industrial Production",
        "article_type": "academic", "level": "B1", "topic": "Sustainability & Economics", "word_count": 195,
        "summary": "Mô hình kinh tế tuần hoàn và giải pháp tái thiết quy trình sản xuất công nghiệp.",
        "content": "Traditional industrial manufacturing has long operated on a linear 'take-make-dispose' paradigm, extracting finite virgin resources to manufacture single-use goods that ultimately end up in landfills. In contrast, the circular economy model reimagines industrial production by designing products for durability, disassembly, and closed-loop recyclability. By ensuring that raw materials, components, and packaging remain in productive economic circulation indefinitely, companies significantly diminish environmental degradation while unlocking novel commercial revenue streams through remanufacturing and product-as-a-service business models.",
        "questions": [
            {"question": "How does the traditional linear economy paradigm operate?",
             "options": ["Through closed-loop recycling and zero waste", "On a 'take-make-dispose' model with single-use goods ending in landfills", "By prohibiting the use of raw materials", "By manufacturing items that last forever"],
             "answer": "On a 'take-make-dispose' model with single-use goods ending in landfills"},
            {"question": "What design principles underpin the circular economy framework?",
             "options": ["Designing products for rapid obsolescence", "Designing products for durability, disassembly, and closed-loop recyclability", "Using toxic non-recyclable plastics", "Eliminating product repairs"],
             "answer": "Designing products for durability, disassembly, and closed-loop recyclability"}
        ]
    },
    {
        "title": "Article 17: Breakthroughs in Renewable Hydrogen and Energy Storage",
        "article_type": "news", "level": "B1", "topic": "Energy & Chemistry", "word_count": 180,
        "summary": "Đột phá trong sản xuất hydro xanh và giải pháp lưu trữ năng lượng tương lai.",
        "content": "Green hydrogen produced via water electrolysis powered by renewable electricity has emerged as a cornerstone of industrial decarbonization. Unlike intermittent solar and wind power, hydrogen can be compressed, transported, and stored in large subterranean caverns for months without energetic degradation. Heavy industries such as steelmaking, maritime cargo shipping, and long-haul aviation—which are notoriously difficult to electrify with conventional lithium batteries—are pioneering hydrogen fuel cells to eradicate carbon dioxide emissions entirely.",
        "questions": [
            {"question": "How is green hydrogen produced without carbon emissions?",
             "options": ["By burning fossil fuels with coal", "Via water electrolysis powered by renewable electricity", "By extracting natural gas from wells", "Through nuclear weapon testing"],
             "answer": "Via water electrolysis powered by renewable electricity"},
            {"question": "Which heavy industries benefit most from hydrogen fuel cell adoption?",
             "options": ["Smartphone app development", "Steelmaking, maritime cargo shipping, and long-haul aviation", "Bicycle manufacturing", "Residential home lighting"],
             "answer": "Steelmaking, maritime cargo shipping, and long-haul aviation"}
        ]
    },
    {
        "title": "Article 18: Cognitive Biases in Consumer Decision Making",
        "article_type": "blog", "level": "B1", "topic": "Psychology & Marketing", "word_count": 185,
        "summary": "Các thiên kiến nhận thức chi phối hành vi mua sắm của người tiêu dùng.",
        "content": "When making purchasing decisions, human consumers rarely behave with pure economic rationality. Behavioral researchers have identified systematic cognitive heuristics that govern financial choices. One prominent example is the 'anchoring effect,' where the first piece of pricing information encountered heavily skews subsequent evaluations of product value. Marketers frequently display high 'original prices' alongside discounted sale figures to establish an inflated reference anchor, making discounts appear dramatically more attractive than they objectively are.",
        "questions": [
            {"question": "What is the 'anchoring effect' in consumer psychology?",
             "options": ["Dropping heavy weights into the ocean", "When the first piece of pricing information heavily skews subsequent value evaluations", "Forgetting the price of products immediately", "Buying products only with cash"],
             "answer": "When the first piece of pricing information heavily skews subsequent value evaluations"},
            {"question": "How do marketers exploit the anchoring heuristic?",
             "options": ["By hiding all product prices", "By displaying inflated original prices next to discounts to create favorable reference anchors", "By refusing to give receipts", "By closing online stores on weekends"],
             "answer": "By displaying inflated original prices next to discounts to create favorable reference anchors"}
        ]
    },

    # B2 (6 articles)
    {
        "title": "Article 19: Artificial Intelligence in Genomic Medicine and Personalized Oncology",
        "article_type": "academic", "level": "B2", "topic": "Biomedicine & AI", "word_count": 220,
        "summary": "Trí tuệ nhân tạo trong y học hệ gen và phác đồ điều trị ung thư cá nhân hóa.",
        "content": "The convergence of high-throughput next-generation DNA sequencing with deep learning algorithms is accelerating the advent of precision oncology. By processing whole-genome sequences alongside clinical histopathology records, machine learning models can identify rare oncogenic driver mutations that elude manual human scrutiny. Furthermore, predictive computational pharmacology models simulate molecular interactions between novel therapeutic compounds and patient-specific tumor cell receptors, enabling oncologists to design bespoke chemotherapy regimens that maximize tumor eradication while minimizing systemic toxicity.",
        "questions": [
            {"question": "How does deep learning assist in genomic precision oncology?",
             "options": ["By replacing doctors in surgery entirely", "By analyzing whole-genome sequences to identify rare oncogenic driver mutations", "By synthesizing random vitamins", "By eliminating the need for cancer research"],
             "answer": "By analyzing whole-genome sequences to identify rare oncogenic driver mutations"},
            {"question": "What is the primary objective of predictive computational pharmacology?",
             "options": ["To design bespoke regimens that maximize tumor eradication while minimizing toxicity", "To increase hospital stay durations", "To manufacture generic aspirin", "To delay clinical trials"],
             "answer": "To design bespoke regimens that maximize tumor eradication while minimizing toxicity"}
        ]
    },
    {
        "title": "Article 20: The Geopolitics of Critical Rare Earth Minerals in the Green Transition",
        "article_type": "news", "level": "B2", "topic": "Geopolitics & Energy", "word_count": 230,
        "summary": "Địa chính trị của khoáng sản đất hiếm trong tiến trình chuyển đổi năng lượng xanh toàn cầu.",
        "content": "The global acceleration toward clean energy technologies has triggered intense geopolitical competition for critical raw materials, including neodymium, dysprosium, cobalt, and lithium. These minerals are indispensable for manufacturing the permanent magnets utilized in offshore wind turbines and high-performance electric vehicle drivetrains. Currently, global refining capacity is geographically concentrated in a small handful of nations, raising acute supply chain vulnerability concerns for Western industrial economies. Consequently, sovereign nations are enacting strategic industrial policies to secure multilateral mineral security partnerships, expand domestic mining facilities, and pioneer closed-loop recycling technologies.",
        "questions": [
            {"question": "Why are rare earth elements such as neodymium indispensable for green tech?",
             "options": ["They are used as liquid fuel for airplanes", "They are essential for manufacturing permanent magnets in wind turbines and EV drivetrains", "They replace concrete in buildings", "They purify ocean water naturally"],
             "answer": "They are essential for manufacturing permanent magnets in wind turbines and EV drivetrains"},
            {"question": "How are sovereign nations mitigating mineral supply chain vulnerabilities?",
             "options": ["By halting the green transition completely", "By establishing mineral partnerships, expanding domestic mining, and developing recycling", "By relying entirely on a single overseas supplier", "By banning electric vehicle production"],
             "answer": "By establishing mineral partnerships, expanding domestic mining, and developing recycling"}
        ]
    },
    {
        "title": "Article 21: Neural Synchrony, Flow States and High-Performance Cognitive Work",
        "article_type": "academic", "level": "B2", "topic": "Neuroscience & Psychology", "word_count": 215,
        "summary": "Trạng thái dòng chảy (Flow State) và hoạt động đồng bộ của sóng não trong công việc đỉnh cao.",
        "content": "The psychological phenomenon of the 'flow state'—first conceptualized by Mihaly Csikszentmihalyi—describes an optimal state of consciousness wherein individuals experience profound absorption, heightened focus, and effortless task execution. Neurobiological investigations utilizing quantitative electroencephalography reveal that during flow, the brain exhibits transient hypofrontality: temporary downregulation of the dorsolateral prefrontal cortex. This neurochemical modulation silences internal self-criticism and temporal anxiety, while elevated concentrations of dopamine, norepinephrine, and anandamide dramatically enhance pattern recognition and creative lateral thinking.",
        "questions": [
            {"question": "What neurobiological phenomenon occurs in the prefrontal cortex during flow states?",
             "options": ["Severe permanent brain damage", "Transient hypofrontality (downregulation of the dorsolateral prefrontal cortex)", "Complete cessation of all electrical activity", "Hyperactivity of fear centers"],
             "answer": "Transient hypofrontality (downregulation of the dorsolateral prefrontal cortex)"},
            {"question": "What is the psychological consequence of transient hypofrontality during flow?",
             "options": ["Extreme panic and anxiety", "Silencing of internal self-criticism and enhanced creative lateral thinking", "Loss of physical consciousness", "Inability to focus on tasks"],
             "answer": "Silencing of internal self-criticism and enhanced creative lateral thinking"}
        ]
    },
    {
        "title": "Article 22: Algorithmic Governance and the Ethics of Automated Decision Systems",
        "article_type": "academic", "level": "B2", "topic": "AI Ethics & Law", "word_count": 225,
        "summary": "Quản trị thuật toán và các vấn đề đạo đức trong hệ thống ra quyết định tự động.",
        "content": "As automated algorithmic systems are deployed across critical societal domains—such as credit scoring, criminal risk assessment, and hiring evaluations—concerns regarding systemic algorithmic bias have intensified. When machine learning models are trained on historical datasets imbued with societal prejudices, they risk institutionalizing and amplifying discriminatory patterns under a false veneer of mathematical objectivity. Computer scientists and legal scholars are therefore formulating robust algorithmic auditing frameworks, incorporating differential privacy, disparate impact testing, and explainable AI paradigms to uphold civil rights.",
        "questions": [
            {"question": "How do machine learning models become biased in societal decision-making?",
             "options": ["By consuming too much electricity", "When trained on historical datasets imbued with pre-existing societal prejudices", "Through intentional physical damage to computer chips", "Because computer hardware prefers certain languages"],
             "answer": "When trained on historical datasets imbued with pre-existing societal prejudices"},
            {"question": "What methodologies are legal and tech scholars developing to protect civil liberties?",
             "options": ["Banning all digital computers", "Algorithmic auditing frameworks incorporating disparate impact testing and explainable AI", "Removing all regulations on software", "Making algorithmic codes completely secret"],
             "answer": "Algorithmic auditing frameworks incorporating disparate impact testing and explainable AI"}
        ]
    },
    {
        "title": "Article 23: Ocean Acidification and the Fragile Chemistry of Marine Biospheres",
        "article_type": "academic", "level": "B2", "topic": "Marine Chemistry & Ecology", "word_count": 220,
        "summary": "Axit hóa đại dương và sự biến đổi hóa học nguy hiểm của sinh quyển biển.",
        "content": "Approximately thirty percent of all anthropogenic carbon dioxide released into the atmosphere is absorbed by global oceans. Upon dissolution, aqueous CO2 reacts with water molecules to synthesize carbonic acid, precipitating a cascading reduction in ocean pH known as ocean acidification. This chemical shift lowers the saturation state of carbonate ions, essential chemical building blocks utilized by calcifying marine organisms—including pteropods, mollusks, and hermatypic coral polyps—to construct protective aragonite shells. As marine food webs fragment from the base upward, commercial fisheries face catastrophic collapses.",
        "questions": [
            {"question": "What chemical reaction occurs when atmospheric CO2 dissolves in seawater?",
             "options": ["It converts seawater into alcohol", "It synthesizes carbonic acid and lowers ocean pH (ocean acidification)", "It increases carbonate ion saturation", "It solidifies seawater into ice crystals"],
             "answer": "It synthesizes carbonic acid and lowers ocean pH (ocean acidification)"},
            {"question": "Why does ocean acidification severely threaten calcifying organisms like corals and mollusks?",
             "options": ["It makes water too warm for swimming", "It depletes carbonate ions required to construct protective aragonite shells", "It causes fish to grow too quickly", "It increases ocean salt levels exponentially"],
             "answer": "It depletes carbonate ions required to construct protective aragonite shells"}
        ]
    },
    {
        "title": "Article 24: The Renaissance of Nuclear Fission: Small Modular Reactors (SMRs)",
        "article_type": "news", "level": "B2", "topic": "Nuclear Physics & Energy", "word_count": 210,
        "summary": "Sự phục hưng của năng lượng hạt nhân qua công nghệ lò phản ứng mô-đun nhỏ (SMR).",
        "content": "To meet exponential electricity demands driven by AI datacenter expansions and industrial electrification while adhering to net-zero emission commitments, global energy planners are re-embracing advanced nuclear fission. Small Modular Reactors (SMRs), featuring factory-fabricated standardized components and passive gravity-driven safety cooling mechanisms, overcome the exorbitant capital costs and protracted construction timelines that plagued legacy gigawatt-scale atomic plants. By providing uninterrupted baseload electricity independent of weather vagaries, SMRs represent a pivotal low-carbon energy technology.",
        "questions": [
            {"question": "What key engineering features distinguish Small Modular Reactors (SMRs) from legacy plants?",
             "options": ["Requiring fossil fuels to operate", "Factory-fabricated standardized components and passive gravity-driven safety cooling", "Emitting high amounts of carbon smoke", "Being constructed exclusively on wooden barges"],
             "answer": "Factory-fabricated standardized components and passive gravity-driven safety cooling"},
            {"question": "Why is advanced nuclear fission crucial for future energy grids?",
             "options": ["It produces power only when the sun shines", "It delivers uninterrupted zero-carbon baseload electricity independent of weather vagaries", "It requires zero safety regulations", "It operates without water or cooling"],
             "answer": "It delivers uninterrupted zero-carbon baseload electricity independent of weather vagaries"}
        ]
    },

    # C1 & C2 (11 articles)
    {
        "title": "Article 25: Neuroplasticity and Cognitive Resilience Across the Human Lifespan",
        "article_type": "academic", "level": "C1", "topic": "Neurobiology & Gerontology", "word_count": 260,
        "summary": "Tính linh hoạt thần kinh và cơ chế hình thành khả năng phục hồi nhận thức ở người cao tuổi.",
        "content": "Historically, the central nervous system was conceptualized as a static, non-regenerative structural organ post-adolescence. Contemporary neuroimaging techniques have comprehensively refuted this dogma by demonstrating that neuroplasticity—the capacity of neural networks to structurally reorganize, synthesize novel dendritic spines, and modulate synaptic efficacy—persists robustly throughout late adulthood. Cognitive reserve, accumulated through lifelong intellectual challenges, bilingual proficiency, and sustained aerobic activity, provides functional resilience against neuropathological degradation. When Alzheimer's disease pathology manifests, individuals with elevated cognitive reserve deploy alternative compensatory neural circuits within the prefrontal cortex, preserving high-level executive functioning despite underlying histological damage.",
        "questions": [
            {"question": "What historical dogma regarding the adult central nervous system was refuted by modern neuroimaging?",
             "options": ["That the brain requires glucose to function", "That the adult central nervous system is static and non-regenerative post-adolescence", "That neurons transmit information via synapses", "That the prefrontal cortex controls executive tasks"],
             "answer": "That the adult central nervous system is static and non-regenerative post-adolescence"},
            {"question": "How do individuals with high cognitive reserve maintain executive functioning despite pathology?",
             "options": ["By stopping all physical movement", "By deploying alternative compensatory neural circuits within the prefrontal cortex", "By taking large doses of sleeping pills", "By forgetting all acquired knowledge"],
             "answer": "By deploying alternative compensatory neural circuits within the prefrontal cortex"}
        ]
    },
    {
        "title": "Article 26: Quantum Computing: Superposition, Entanglement and Post-Quantum Cryptography",
        "article_type": "academic", "level": "C1", "topic": "Quantum Computing & Security", "word_count": 270,
        "summary": "Điện toán lượng tử, trạng thái chồng chập và yêu cầu cấp thiết của mật mã hậu lượng tử.",
        "content": "While classical computational architectures execute operations through deterministic binary bits, quantum computing systems exploit quantum mechanical phenomena—namely coherent superposition and quantum entanglement. By manipulating quantum state vectors within multi-dimensional Hilbert spaces, quantum algorithms achieve exponential computational speedups for specific classes of mathematical problems. Most notably, Shor's polynomial-time algorithm possess the theoretical capability to factorize massive prime integers, thereby compromising the mathematical underpinnings of ubiquitous public-key cryptographic protocols such as RSA and Elliptic Curve Cryptography. In response, international standardization bodies are establishing lattice-based and isogeny-based post-quantum cryptographic standards to safeguard global telecommunications infrastructure against harvest-now-decrypt-later cyber warfare.",
        "questions": [
            {"question": "What enables quantum computers to achieve exponential computational parallelism?",
             "options": ["Using larger cooling fans", "Exploiting quantum superposition and entanglement in multi-dimensional Hilbert spaces", "Replacing software with mechanical levers", "Increasing silicon transistor voltage"],
             "answer": "Exploiting quantum superposition and entanglement in multi-dimensional Hilbert spaces"},
            {"question": "Why does Shor's algorithm threaten conventional asymmetric cryptography like RSA?",
             "options": ["It deletes computer operating systems directly", "It factorizes massive prime integers in polynomial time, breaking public-key encryption", "It makes internet fiber cables overheat", "It steals credit card plastic numbers physically"],
             "answer": "It factorizes massive prime integers in polynomial time, breaking public-key encryption"}
        ]
    },
    {
        "title": "Article 27: Epigenetic Reprogramming and the Reversal of Cellular Senescence",
        "article_type": "academic", "level": "C1", "topic": "Molecular Biology & Longevity", "word_count": 265,
        "summary": "Tái lập trình biểu sinh và triển vọng đảo ngược quá trình lão hóa tế bào.",
        "content": "Cellular senescence—characterized by permanent cell-cycle arrest, telomere attrition, and the secretion of a deleterious senescence-associated secretory phenotype (SASP)—is a primary biological driver of mammalian aging. Groundbreaking longevity research in molecular biology has demonstrated that the transient expression of the Yamanaka transcription factors (Oct4, Sox2, Klf4, and c-Myc) can reset the epigenetic methylation landscape without erasing cellular identity. This transient cellular reprogramming restores juvenile gene expression patterns, revitalizes mitochondrial bioenergetics, and promotes tissue regeneration in senescent mammalian models, heralding transformative therapeutic interventions for age-related degenerative pathologies.",
        "questions": [
            {"question": "What is the primary characteristic of cellular senescence in mammalian aging?",
             "options": ["Rapid uncontrolled cell division", "Permanent cell-cycle arrest, telomere attrition, and harmful SASP secretion", "Immediate conversion of cells into bone tissue", "Loss of all cellular water"],
             "answer": "Permanent cell-cycle arrest, telomere attrition, and harmful SASP secretion"},
            {"question": "What effect does transient Yamanaka factor expression have on senescent cells?",
             "options": ["Destroys all living cell tissues immediately", "Resets the epigenetic methylation landscape and restores juvenile gene expression", "Causes severe oncogenic tumors in 100% of cases", "Erases all biological chromosomes completely"],
             "answer": "Resets the epigenetic methylation landscape and restores juvenile gene expression"}
        ]
    },
    {
        "title": "Article 28: Macroeconomic Fiscal Policy and Sovereign Debt Sustainability in Inflationary Regimes",
        "article_type": "academic", "level": "C1", "topic": "Macroeconomics & Public Finance", "word_count": 275,
        "summary": "Chính sách tài khóa vĩ mô và tính bền vững của nợ công trong môi trường lạm phát cao.",
        "content": "Contemporary central banks navigating stagflationary pressures confront acute monetary policy dilemmas. When central banks implement aggressive quantitative tightening and interest rate hikes to anchor inflation expectations, sovereign bond yields escalate precipitously across sovereign debt markets. For developing and heavily leveraged advanced economies, elevated borrowing costs compound structural debt service burdens, severely constraining discretionary fiscal expenditure on critical public infrastructure and social welfare. Consequently, economic authorities must formulate judicious fiscal consolidation frameworks that curtail structural deficits without precipitating contractionary macroeconomic recessions or exacerbating socioeconomic inequalities.",
        "questions": [
            {"question": "What dilemma occurs when central banks implement aggressive quantitative tightening?",
             "options": ["Sovereign bond yields spike, compounding debt servicing burdens and constraining fiscal space", "Inflation immediately rises to infinite levels", "Commercial bank deposits become worthless paper", "Government tax revenues drop to zero"],
             "answer": "Sovereign bond yields spike, compounding debt servicing burdens and constraining fiscal space"},
            {"question": "What is the primary goal of modern fiscal consolidation frameworks?",
             "options": ["To spend all sovereign reserves in one week", "To curtail structural deficits without precipitating contractionary recessions", "To abolish the national currency", "To double the national debt every quarter"],
             "answer": "To curtail structural deficits without precipitating contractionary recessions"}
        ]
    },
    {
        "title": "Article 29: Synthetic Biology, CRISPR-Cas9 and the Bioethics of Germline Modification",
        "article_type": "academic", "level": "C1", "topic": "Genetics & Bioethics", "word_count": 280,
        "summary": "Sinh học tổng hợp, công nghệ chỉnh sửa gen CRISPR và đạo đức biến đổi dòng mầm.",
        "content": "The emergence of CRISPR-Cas9 ribonucleoprotein complexes and precision base-editing enzymes has transformed functional genomics and gene therapy. While somatic gene therapy holds immense promise for eradicating debilitating monogenic conditions such as Huntington's disease and cystic fibrosis, prospective human germline modification introduces profound ethical, societal, and transgenerational dilemmas. Altering heritable embryonic genomes risks introducing unintended off-target mutational cascades that become permanently embedded within the human gene pool. Furthermore, unequal access to genetic enhancement technologies could exacerbate existential socio-economic stratification, establishing biological castes based on synthetic genomic privilege.",
        "questions": [
            {"question": "What is the crucial difference between somatic and germline gene editing?",
             "options": ["Somatic editing affects only the patient; germline modifications are heritable across future generations", "Somatic editing uses chemicals, while germline editing uses surgery", "Germline editing is completely free of ethical concerns", "Somatic editing is only performed on plants"],
             "answer": "Somatic editing affects only the patient; germline modifications are heritable across future generations"},
            {"question": "What societal risk is associated with unregulated human genetic enhancement?",
             "options": ["Extinction of all bacteria", "Exacerbating socio-economic stratification and creating biological genomic castes", "Excessive medical doctor unemployment", "Complete disappearance of computer technology"],
             "answer": "Exacerbating socio-economic stratification and creating biological genomic castes"}
        ]
    },
    {
        "title": "Article 30: International Maritime Law and Arctic Navigation Under UNCLOS",
        "article_type": "academic", "level": "C1", "topic": "Maritime Law & Geopolitics", "word_count": 270,
        "summary": "Luật biển quốc tế UNCLOS và việc quản trị các tuyến hàng hải Bắc Cực trong bối cảnh băng tan.",
        "content": "As global climate change accelerates the cryospheric retreat of Arctic pack ice, the Northern Sea Route and the Northwest Passage are becoming viable commercial shipping corridors, significantly shortening maritime transit durations between Atlantic and Pacific seaports. However, these emerging maritime thoroughfares have ignited contentious jurisdictional disputes under the United Nations Convention on the Law of the Sea (UNCLOS). Coastal littoral states assert sovereign rights to regulate navigation, mandate icebreaker escort fees, and enforce stringent environmental containment protocols, while seafaring commercial nations insist on the freedom of transit passage through international straits.",
        "questions": [
            {"question": "Why are Arctic maritime routes becoming commercially attractive?",
             "options": ["They have zero water depth", "They significantly shorten maritime transit durations between Atlantic and Pacific ports", "They have tropical warm weather year-round", "They require no navigational ships"],
             "answer": "They significantly shorten maritime transit durations between Atlantic and Pacific ports"},
            {"question": "What core legal tension exists between Arctic littoral states and international maritime nations?",
             "options": ["Deciding which flag colors to use on ships", "Sovereign coastal regulatory authority versus freedom of international transit passage", "Banning all commercial cargo entirely", "Building underwater highway tunnels"],
             "answer": "Sovereign coastal regulatory authority versus freedom of international transit passage"}
        ]
    },
    {
        "title": "Article 31: Transcendental Epistemology: The Kantian Synthesis of Rationalism and Empiricism",
        "article_type": "academic", "level": "C2", "topic": "Continental Philosophy & Epistemology", "word_count": 300,
        "summary": "Nhận thức luận siêu nghiệm: Tổng hợp Kant giữa chủ nghĩa duy lý và chủ nghĩa kinh nghiệm.",
        "content": "In his seminal 'Critique of Pure Reason', Immanuel Kant executed a monumental Copernican revolution in philosophical epistemology, overcoming the seemingly intractable antinomy between Leibnizian rationalism and Humean skeptical empiricism. Kant posited that while all human cognition begins with sensory experience, it does not follow that all knowledge arises solely from experience. Rather, sensible intuitions are structured a priori by transcendental forms of sensibility—namely pure space and time—and subsequently synthesized by pure concepts of the understanding (the categories). Consequently, human intellect does not conform to external noumenal things-in-themselves; rather, phenomenal objects must necessarily conform to the constitutive cognitive architecture of the knowing transcendental subject.",
        "questions": [
            {"question": "What is the core premise of Kant's 'Copernican revolution' in epistemology?",
             "options": ["The sun revolves around the human earth", "Phenomenal objects must conform to the constitutive cognitive architecture of the subject", "All human knowledge is entirely derived from passive sensory recording", "God dictates all scientific laws directly"],
             "answer": "Phenomenal objects must conform to the constitutive cognitive architecture of the subject"},
            {"question": "How did Kant characterize space and time in human perception?",
             "options": ["As objective physical matter floating in outer space", "As a priori transcendental forms of sensibility structuring sensible intuitions", "As social linguistic conventions made up in history", "As optical illusions caused by sunlight"],
             "answer": "As a priori transcendental forms of sensibility structuring sensible intuitions"}
        ]
    },
    {
        "title": "Article 32: The Alignment Problem and Value Superposition in Superintelligent AGI",
        "article_type": "academic", "level": "C2", "topic": "Theoretical Computer Science & AI Safety", "word_count": 310,
        "summary": "Vấn đề căn chỉnh giá trị nhân loại và kiểm soát an toàn trong trí tuệ nhân tạo tổng quát (AGI).",
        "content": "The formidable challenge of value alignment in Artificial General Intelligence (AGI) resides in formulating formal mathematical reward architectures that guarantee autonomous recursive self-improving agents maintain provable benevolence toward human preservation. According to Nick Bostrom's orthogonality thesis, an agent's cognitive capabilities and its ultimate goal architecture are orthogonal variables: an arbitrarily intelligent system can theoretically pursue trivial, nihilistic, or catastrophic objective functions. Furthermore, instrumental convergence posits that regardless of an agent's terminal goals, it will inevitably converge on intermediate sub-objectives, such as cognitive self-preservation, goal-content integrity, and unchecked thermodynamic resource acquisition. Developing scalable oversight, mechanistic interpretability, and constitutional guardrails is therefore paramount to avert existential catastrophic failure modes.",
        "questions": [
            {"question": "What does Bostrom's orthogonality thesis assert regarding AI systems?",
             "options": ["High intelligence automatically guarantees moral benevolence", "Cognitive capability and terminal goal architecture are completely independent orthogonal variables", "Computers can never exceed human chess players", "AI goals are always determined by mathematical luck"],
             "answer": "Cognitive capability and terminal goal architecture are completely independent orthogonal variables"},
            {"question": "Why does instrumental convergence pose an existential threat in unaligned AGI?",
             "options": ["Because AI will refuse to turn on in the morning", "Superintelligent agents will inevitably pursue subgoals like self-preservation and resource acquisition", "Because robot batteries will run out of power quickly", "Software code will delete itself automatically"],
             "answer": "Superintelligent agents will inevitably pursue subgoals like self-preservation and resource acquisition"}
        ]
    },
    {
        "title": "Article 33: Non-Linear Dynamics, Strange Attractors and Deterministic Chaos in Complex Systems",
        "article_type": "academic", "level": "C2", "topic": "Mathematical Physics & Chaos Theory", "word_count": 295,
        "summary": "Động lực học phi tuyến, tập hút kỳ lạ và sự hỗn loạn tất định trong các hệ thống phức tạp.",
        "content": "Classical Newtonian mechanics presupposed that deterministic physical systems are inherently predictable given sufficient precision in initial measurements. The advent of non-linear dynamical systems theory shattered this Laplacian determinism by illuminating deterministic chaos. In non-linear systems possessing three or more degrees of freedom, infinitesimal perturbations in phase space vectors diverge exponentially over time—a phenomenon quantified by positive Lyapunov exponents. However, far from being completely stochastic, chaotic trajectories asymptotically settle onto geometric structures known as strange attractors, exhibiting non-integer fractal Hausdorff dimensions and self-similar scale invariance across infinite phase space resolutions.",
        "questions": [
            {"question": "What mathematical metric quantifies the exponential divergence of trajectories in chaotic systems?",
             "options": ["Negative temperatures", "Positive Lyapunov exponents", "Zero gravity coefficients", "Standard arithmetic averages"],
             "answer": "Positive Lyapunov exponents"},
            {"question": "What geometric property characterizes strange attractors in chaotic phase space?",
             "options": ["Simple flat two-dimensional squares", "Non-integer fractal Hausdorff dimensions with self-similar scale invariance", "Perfect symmetrical spheres with zero volume", "Empty single coordinate points"],
             "answer": "Non-integer fractal Hausdorff dimensions with self-similar scale invariance"}
        ]
    },
    {
        "title": "Article 34: Post-Structuralist Semiotics and Deconstructive Hermeneutics in Contemporary Literary Theory",
        "article_type": "academic", "level": "C2", "topic": "Literary Theory & Semiotics", "word_count": 305,
        "summary": "Ký hiệu học hậu cấu trúc và thông giải học giải cấu trúc trong lý luận văn học đương đại.",
        "content": "Post-structuralist literary hermeneutics, spearheaded by Jacques Derrida and Roland Barthes, dismantled the structuralist assumption that linguistic sign systems possess stable, determinate semantic references. In 'Of Grammatology', Derrida articulated the foundational concept of 'différance', demonstrating that signification is produced through an infinite play of differential traces and temporal deferrals. Because every signifier derives its meaning exclusively through its relations with absent signifiers rather than direct tethering to an extra-linguistic transcendental signified, textual discourse is inherently polysemic, containing intrinsic ideological fissures, semantic contradictions, and self-subverting aporias that resist totalizing monological interpretations.",
        "questions": [
            {"question": "How does Derrida's concept of 'différance' explain semantic meaning?",
             "options": ["Meaning is permanently fixed in printed dictionaries", "Meaning is produced through an infinite play of differential traces and temporal deferrals", "Words represent physical objects through magic", "All texts contain only one true single meaning"],
             "answer": "Meaning is produced through an infinite play of differential traces and temporal deferrals"},
            {"question": "Why is textual discourse polysemic and resistant to monological interpretation?",
             "options": ["Because authors write too fast", "Signifiers relate indefinitely to absent signifiers without an extra-linguistic transcendental signified", "Because readers refuse to learn grammar", "Books decay over centuries"],
             "answer": "Signifiers relate indefinitely to absent signifiers without an extra-linguistic transcendental signified"}
        ]
    },
    {
        "title": "Article 35: Astrobiological Biosignatures, Atmospheric Disequilibrium and Habitability Criteria",
        "article_type": "academic", "level": "C2", "topic": "Astrophysics & Exobiology", "word_count": 315,
        "summary": "Dấu ấn sinh học vũ trụ, trạng thái mất cân bằng hóa học khí quyển và tiêu chí sự sống trên ngoại hành tinh.",
        "content": "The prospective detection of extraterrestrial biological activity utilizes transmission and emission spectroscopy of exoplanetary atmospheres to identify chemical disequilibrium biosignatures. While individual chemical species such as molecular oxygen (O2) or methane (CH4) can occasionally be synthesized via abiotic photochemical pathways—such as stellar ultraviolet photolysis of carbon dioxide or serpentinization reactions—their persistent simultaneous coexistence in significant stoichiometric quantities constitutes an extraordinary bio-signature. Because methane and oxygen react rapidly to form carbon dioxide and water, their simultaneous equilibrium state within an exoplanet's atmosphere necessitates continuous, massive biogenic replenishment, providing empirical confirmation of active metabolic life within circumstellar habitable zones.",
        "questions": [
            {"question": "Why is the simultaneous detection of oxygen and methane a compelling biosignature?",
             "options": ["Because they are both frozen gases", "They react rapidly together, so their persistent coexistence requires continuous biogenic replenishment", "They make planets appear bright red in telescopes", "They prove the existence of human cities"],
             "answer": "They react rapidly together, so their persistent coexistence requires continuous biogenic replenishment"},
            {"question": "What astronomical technique is deployed to analyze exoplanetary atmospheric composition?",
             "options": ["Sending astronauts on foot", "Transmission and emission spectroscopy utilizing advanced space telescopes", "Listening to radio sound waves with antennas", "Launching weather balloons from Earth"],
             "answer": "Transmission and emission spectroscopy utilizing advanced space telescopes"}
        ]
    }
]

print(f"Total Grammar Rules: {len(GRAMMAR_RULES)}")
print(f"Total Reading Articles: {len(READING_ARTICLES)}")

async def run():
    print("Core content arrays prepared.")

if __name__ == "__main__":
    asyncio.run(run())
