"""
scripts/build_part1.py
Constructs MEGA_PART1 for Topics 2-32 top-ups.
"""

import sys
import json
from pathlib import Path

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent.parent
OUT_FILE = BASE_DIR / "scripts" / "data" / "mega_part1_topups.py"

print("Building Part 1 Top-ups...")

# Term definitions
# Tuple format: (word, ipa, pos, lvl, vi, en, ex_en, ex_vi, syn, col, mne)
TOPUPS = {
    "Food, Cooking & Dining": [
        ("caramelize", "/ˈker.ə.məl.aɪz/", "verb", "B2", "Thắng đường, caramel hóa bề mặt", "Cook sugar or food until it turns brown and sweet.", "Caramelize the onions slowly over low heat.", "Thắng hành tây từ từ trên lửa nhỏ.", ["brown", "glaze"], ["caramelize onions", "slowly caramelize"], "💡 Thắng đường thành caramel."),
        ("poach", "/poʊtʃ/", "verb", "B1", "Chần trong nước lăn tăn", "Cook food gently in simmering liquid.", "Poached eggs on toast are a nutritious breakfast.", "Trứng chần trên bánh mì nướng là bữa sáng bổ dưỡng.", ["simmer", "coddle"], ["poach eggs", "poached salmon"], "💡 Chần chín mềm trong nước sôi nhẹ."),
        ("marinate", "/ˈmer.ə.neɪt/", "verb", "B1", "Tẩm ướp gia vị cho ngấm", "Soak food in seasoned liquid before cooking.", "Marinate the meat overnight for deep flavor.", "Tẩm ướp thịt qua đêm để ngấm gia vị sâu.", ["season", "steep"], ["marinate overnight", "marinate meat"], "💡 Ướp thịt với marinade."),
        ("julienne", "/ˌdʒuː.liˈen/", "verb", "B2", "Thái sợi chỉ mỏng dài", "Cut vegetables into thin matchstick strips.", "Julienne the bell peppers for the summer salad.", "Thái sợi ớt chuông để làm món salad mùa hè.", ["shred", "thin slice"], ["julienne carrots", "fine julienne"], "💡 Thái sợi kiểu Pháp như que diêm.")
    ],
    "Travel, Tourism & Transportation": [
        ("layover", "/ˈleɪˌoʊ.vɚ/", "noun", "B1", "Thời gian quá cảnh chờ nối chuyến", "A period of rest or waiting between flight legs.", "We had a four-hour layover at Incheon Airport.", "Chúng tôi quá cảnh bốn tiếng tại sân bay Incheon.", ["stopover", "transit"], ["long layover", "flight layover"], "💡 Dừng nghỉ tại sân bay chờ chuyến bay kế."),
        ("itinerary", "/aɪˈtɪn.ə.rer.i/", "noun", "B1", "Lịch trình chi tiết chuyến đi", "A planned route or journey with scheduled dates.", "The tour guide distributed the printed itinerary to everyone.", "Hướng dẫn viên đã phát bản in lịch trình cho tất cả mọi người.", ["schedule", "travel plan"], ["detailed itinerary", "travel itinerary"], "💡 Lộ trình chi tiết từng ngày."),
        ("jet lag", "/ˈdʒet ˌlæɡ/", "noun", "B1", "Mệt mỏi do lệch múi giờ bay xa", "Tiredness felt after a flight across time zones.", "Hydration helps overcome the effects of severe jet lag.", "Uống đủ nước giúp vượt qua cảm giác mệt mỏi do lệch múi giờ.", ["fatigue", "time lag"], ["suffer jet lag", "overcome jet lag"], "💡 Cơ thể bị trễ nhịp sau chuyến bay dài."),
        ("carry-on", "/ˈker.i.ɑːn/", "noun", "A2", "Hành lý xách tay lên máy bay", "Small baggage brought into the aircraft cabin.", "Only one carry-on bag is permitted per economy passenger.", "Mỗi hành khách phổ thông chỉ được mang một kiện hành lý xách tay.", ["cabin baggage", "hand luggage"], ["carry-on bag", "carry-on luggage"], "💡 Kiện hành lý tự xách theo người.")
    ],
    "Technology & Artificial Intelligence": [
        ("latency", "/ˈleɪ.tən.si/", "noun", "B2", "Độ trễ truyền dữ liệu mạng", "Delay before a transfer of data begins.", "Low network latency is critical for interactive online games.", "Độ trễ mạng thấp là yếu tố then chốt cho các trò chơi trực tuyến tương tác.", ["lag", "delay"], ["low latency", "network latency"], "💡 Thời gian chờ phản hồi của hệ thống."),
        ("throughput", "/ˈθruː.pʊt/", "noun", "B2", "Thông lượng dữ liệu qua hệ thống", "The amount of data processed in a given period.", "The fiber-optic cable maximized real-time data throughput.", "Cáp quang đã tối đa hóa thông lượng dữ liệu thời gian thực.", ["bandwidth", "capacity"], ["data throughput", "high throughput"], "💡 Lượng dữ liệu đi xuyên qua hệ thống mỗi giây.")
    ],
    "Business, Management & Workplace": [
        ("stakeholder", "/ˈsteɪkˌhoʊl.dɚ/", "noun", "B2", "Bên liên quan trong doanh nghiệp", "A person with an interest or concern in a business.", "Management consulted all key stakeholders before the merger.", "Ban điều hành đã tham vấn tất cả các bên liên quan chủ chốt trước vụ sáp nhập.", ["shareholder", "partner"], ["key stakeholder", "stakeholder engagement"], "💡 Người nắm giữ quyền lợi trong dự án."),
        ("deliverable", "/dɪˈlɪv.ɚ.ə.bəl/", "noun", "B2", "Sản phẩm/kết quả bàn giao", "A tangible product produced as a result of a project.", "The software prototype was the primary deliverable for Q1.", "Bản mẫu phần mềm là sản phẩm bàn giao chính trong quý 1.", ["output", "product"], ["project deliverable", "final deliverable"], "💡 Thứ bàn giao cho khách hàng khi hoàn thành.")
    ],
    "Education & Academic Life": [
        ("dissertation", "/ˌdɪs.ɚˈteɪ.ʃən/", "noun", "B2", "Luận văn thạc sĩ hoặc tiến sĩ", "A long essay written for a university degree.", "Her doctoral dissertation examined climate change economics.", "Luận án tiến sĩ của cô ấy nghiên cứu kinh tế học biến đổi khí hậu.", ["thesis", "treatise"], ["doctoral dissertation", "submit dissertation"], "💡 Công trình nghiên cứu học thuật cấp cao."),
        ("curriculum", "/kəˈrɪk.jə.ləm/", "noun", "B2", "Khung chương trình đào tạo", "The subjects comprising a course of study.", "The high school revised its science curriculum this semester.", "Trường trung học đã sửa đổi khung chương trình khoa học trong học kỳ này.", ["syllabus", "study plan"], ["core curriculum", "school curriculum"], "💡 Lộ trình các môn học cần hoàn thành.")
    ],
    "Shopping, Fashion & Retail": [
        ("haute couture", "/ˌoʊt kuːˈtʊr/", "noun", "C1", "Thời trang cao cấp may đo riêng", "High-end fashion design and custom garment construction.", "The French fashion house debuted its autumn haute couture line.", "Nhà mốt Pháp đã ra mắt dòng thời trang cao cấp may đo mùa thu.", ["high fashion", "custom design"], ["haute couture show", "couture dress"], "💡 Thời trang độc bản xa xỉ bậc nhất."),
        ("bespoke", "/bɪˈspoʊk/", "adjective", "B2", "May đo thủ công theo yêu cầu riêng", "Custom-made to the specifications of an individual.", "He ordered a bespoke wool suit for his wedding day.", "Anh ấy đặt may riêng một bộ âu phục dạ cho ngày cưới.", ["custom-made", "tailor-made"], ["bespoke suit", "bespoke design"], "💡 Đặt may riêng theo số đo chuẩn xác."),
        ("bargain hunter", "/ˈbɑːr.ɡɪn ˌhʌn.t̬ɚ/", "noun", "B1", "Người săn hàng giảm giá", "A shopper seeking out items at discount prices.", "Bargain hunters filled the mall during the annual clearance event.", "Những người săn hàng giảm giá chen kín trung tâm thương mại trong dịp xả kho hàng năm.", ["deal seeker", "shopper"], ["savvy bargain hunter", "attract bargain hunters"], "💡 Người chuyên lùng sục các món đồ giá hời."),
        ("clearance sale", "/ˈklɪr.əns ˌseɪl/", "noun", "B1", "Đợt bán thanh lý xả kho", "Sale intended to sell off remaining inventory.", "The store advertised a 70% clearance sale on winter coats.", "Cửa hàng thông báo giảm giá xả kho 70% đối với áo khoác mùa đông.", ["liquidation sale", "inventory clearance"], ["annual clearance sale", "clearance discounts"], "💡 Dọn sạch kho để đón đợt hàng mới.")
    ]
}

print(f"Top-ups prepared for base topics.")
