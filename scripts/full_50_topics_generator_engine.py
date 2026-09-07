"""
scripts/full_50_topics_generator_engine.py
Comprehensive generator that populates all 50 Topics with authentic English vocabulary,
bilingual definitions, phonetics, and structured learning attributes.
"""

import sys
from pathlib import Path

# Add scripts to sys.path
sys.path.append(str(Path(__file__).parent))

# Import expansion catalog
from domain_expansion_catalog import add_terms

# Topic 23: Hospitality, Hotel & Customer Service
add_terms("Hospitality, Hotel & Customer Service", [
    ("bellhop", "/ˈbel.hɑːp/", "noun", "A2", "Nhân viên xách hành lý khách sạn", "A staff member in a hotel who carries luggage for guests."),
    ("valet parking", "/vælˈeɪ ˌpɑːr.kɪŋ/", "noun", "B1", "Dịch vụ đỗ xe hộ cho khách", "A service in which an attendant parks your car for you at a hotel or restaurant."),
    ("turndown service", "/ˈtɝːn.daʊn ˌsɝː.vɪs/", "noun", "B2", "Dịch vụ trải lại giường buổi tối trong khách sạn", "A hotel service where a housekeeper prepares the bed for sleeping in the evening."),
    ("suite", "/swiːt/", "noun", "A2", "Phòng căn hộ cao cấp trong khách sạn", "A set of connected rooms, especially in a hotel, forming one unit."),
    ("amenities", "/əˈmen.ə.t̬iz/", "noun", "B1", "Tiện nghi tiện ích phục vụ khách", "Desirable or useful features of a building or place, such as pools or gym."),
    ("adjoining rooms", "/əˈdʒɔɪ.nɪŋ ˌruːmz/", "noun", "B1", "Hai phòng khách sạn thông nhau qua cửa trong", "Two hotel rooms with a private door connecting them directly."),
    ("complimentary", "/ˌkɑːm.pləˈmen.t̬ɚ.i/", "adjective", "B1", "Được miễn phí chiêu đãi (bữa sáng, nước uống)", "Given or supplied free of charge as a courtesy."),
    ("check-out", "/ˈtʃek.aʊt/", "noun", "A1", "Thủ tục trả phòng khách sạn", "The action of vacating and paying for one's hotel room."),
    ("vacancy", "/ˈveɪ.kən.si/", "noun", "A2", "Phòng trống có thể đặt", "An unoccupied room in a hotel or guesthouse."),
    ("hospitality", "/ˌhɑː.spɪˈtæl.ə.t̬i/", "noun", "B1", "Ngành lòng hiếu khách và dịch vụ khách hàng", "The friendly and generous reception and entertainment of guests or strangers."),
    ("reservation", "/ˌrez.ɚˈveɪ.ʃən/", "noun", "A2", "Sự đặt phòng/bàn trước", "An arrangement by which something is secured in advance."),
    ("concierge desk", "/koʊn.siˈerʒ ˌdesk/", "noun", "B2", "Bàn hướng dẫn và hỗ trợ khách du lịch tại sảnh", "A hotel service counter assisting guests with bookings, tours, and advice."),
    ("housekeeping", "/ˈhaʊsˌkiː.pɪŋ/", "noun", "A2", "Bộ phận buồng phòng dọn dẹp phòng ốc", "The management of household affairs or cleaning hotel rooms."),
    ("minibar", "/ˈmɪn.i.bɑːr/", "noun", "A2", "Tủ lạnh nhỏ chứa đồ uống có tính phí trong phòng", "A small refrigerator in a hotel room containing beverages and snacks."),
    ("master key", "/ˈmæs.tɚ ˌkiː/", "noun", "B1", "Chìa khóa vạn năng mở được mọi phòng", "A key that opens several different locks in a hotel."),
    ("doorman", "/ˈdɔːr.mən/", "noun", "A2", "Nhân viên gác cửa đón tiếp khách", "A person who guards the entrance to a large building or hotel."),
    ("in-room dining", "/ˌɪn ruːm ˈdaɪ.nɪŋ/", "noun", "A2", "Dịch vụ phục vụ bữa ăn tận phòng (Room Service)", "Food and drink delivered to a guest's private hotel room."),
    ("late check-out", "/ˌleɪt ˈtʃek.aʊt/", "noun", "B1", "Được trả phòng muộn hơn giờ quy định", "An arrangement allowing a hotel guest to leave later than standard time."),
    ("guest satisfaction", "/ˈɡest ˌsæt̬.ɪsˌfæk.ʃən/", "noun", "B2", "Sự hài lòng tuyệt đối của khách hàng", "A measurement of how services supplied by a hotel meet or surpass customer expectations."),
    ("patron", "/ˈpeɪ.trən/", "noun", "B2", "Khách hàng quen thuộc thường xuyên lui tới", "A customer, especially a regular one, of a store, restaurant, or theater.")
])

# Topic 24: Culture, Traditions & Festivals
add_terms("Culture, Traditions & Festivals", [
    ("heritage", "/ˈher.ə.t̬ɪdʒ/", "noun", "B1", "Di sản văn hóa truyền đời của dân tộc", "Property that is or may be inherited; valued objects and qualities passed down from previous generations."),
    ("folklore", "/ˈfoʊk.lɔːr/", "noun", "B1", "Văn hóa dân gian, truyện kể dân gian", "The traditional beliefs, customs, and stories of a community, passed through the generations by word of mouth."),
    ("ritual", "/ˈrɪtʃ.u.əl/", "noun", "B2", "Nghi lễ tâm linh truyền thống tôn nghiêm", "A religious or solemn ceremony consisting of a series of actions performed according to a prescribed order."),
    ("festivity", "/fesˈtɪv.ə.t̬i/", "noun", "B1", "Hoạt động vui chơi lễ hội rộn ràng", "The celebration of something in a joyful and exuberant way."),
    ("carnival", "/ˈkɑːr.nə.vəl/", "noun", "B1", "Lễ hội hóa trang đường phố rực rỡ", "A period of public revelry at a regular time each year, involving processions and music."),
    ("customary", "/ˈkʌs.tə.mer.i/", "adjective", "B2", "Theo phong tục tập quán lệ thường", "According to the customs or usual practices associated with a particular society."),
    ("indigenous", "/ɪnˈdɪdʒ.ə.nəs/", "adjective", "B2", "Thuộc về người bản địa thổ dân nguyên thủy", "Originating or occurring naturally in a particular place; native."),
    ("artifact", "/ˈɑːr.t̬ə.fækt/", "noun", "B1", "Cổ vật hiện vật văn hóa khảo cổ", "An object made by a human being, typically an item of cultural or historical interest."),
    ("costume", "/ˈkɑː.stuːm/", "noun", "A2", "Trang phục truyền thống hoặc hóa trang", "A set of clothes in a style typical of a particular country or period."),
    ("procession", "/prəˈseʃ.ən/", "noun", "B1", "Đoàn người rước lễ diễu hành trang trọng", "A number of people or vehicles moving forward in an orderly fashion."),
    ("commemoration", "/kəˌmem.əˈreɪ.ʃən/", "noun", "B2", "Lễ tưởng niệm công ơn tiền nhân", "Remembrance, typically expressed in a ceremony."),
    ("pilgrim", "/ˈpɪl.ɡrɪm/", "noun", "B2", "Người hành hương về đất thánh linh thiêng", "A person who journeys to a sacred place for religious reasons."),
    ("superstition", "/ˌsuː.pɚˈstɪʃ.ən/", "noun", "B2", "Tập tục mê tín dị đoan truyền miệng", "Excessively credulous belief in and reverence for supernatural beings or omens."),
    ("taboo", "/təˈbuː/", "noun", "B2", "Điều cấm kỵ kiêng khem trong văn hóa", "A social or religious custom prohibiting or forbidding discussion of a practice."),
    ("pagan", "/ˈpeɪ.ɡən/", "noun", "C1", "Người theo tín ngưỡng đa thần tự nhiên cổ", "A person holding religious beliefs other than those of the main world religions."),
    ("solstice", "/ˈsɑːl.stɪs/", "noun", "B2", "Ngày hạ chí hoặc đông chí trong năm", "Either of the two times in the year, summer or winter, when the sun reaches its highest or lowest point."),
    ("equinox", "/ˈiː.kwə.nɑːks/", "noun", "B2", "Ngày xuân phân hoặc thu phân (ngày dài bằng đêm)", "The time or date twice each year at which the sun crosses the celestial equator, when day and night are of equal length."),
    ("pageantry", "/ˈpædʒ.ən.tri/", "noun", "C1", "Sự phô diễn nghi thức lễ hội lộng lẫy hoành tráng", "Elaborate display or ceremony."),
    ("ancestor worship", "/ˈæn.ses.tɚ ˌwɝː.ʃɪp/", "noun", "B1", "Tín ngưỡng thờ cúng tổ tiên cội nguồn", "The custom of venerating deceased ancestors who are considered still to be part of the family."),
    ("incense", "/ˈɪn.sens/", "noun", "B1", "Nén hương thơm dâng lên bàn thờ", "A gum, spice, or other substance that is burned for the sweet smell it produces.")
])

# Topic 25: Hobbies, Leisure & Creative Skills
add_terms("Hobbies, Leisure & Creative Skills", [
    ("calligraphy", "/kəˈlɪɡ.rə.fi/", "noun", "B2", "Nghệ thuật thư pháp chữ đẹp nét mực", "Decorative handwriting or handwritten lettering with ink."),
    ("origami", "/ˌɔːr.ɪˈɡɑː.mi/", "noun", "A2", "Nghệ thuật gấp giấy truyền thống Nhật Bản", "The Japanese art of folding paper into decorative shapes and figures."),
    ("pottery", "/ˈpɑː.t̬ɚ.i/", "noun", "A2", "Nghệ thuật làm đồ gốm trên bàn xoay", "Pots, dishes, and other articles made of earthenware or baked clay."),
    ("ceramics", "/səˈræm.ɪks/", "noun", "B1", "Đồ gốm sứ tráng men nung lò", "Pots and other articles made from clay hardened by heat."),
    ("woodworking", "/ˈwʊdˌwɝː.kɪŋ/", "noun", "B1", "Nghề mộc chạm khắc chế tác gỗ", "The activity or skill of making things from wood."),
    ("gardening", "/ˈɡɑːr.dən.ɪŋ/", "noun", "A1", "Thú vui làm vườn trồng hoa cây cảnh", "The activity of tending and cultivating a garden."),
    ("horticulture", "/ˈhɔːr.t̬əˌkʌl.tʃɚ/", "noun", "C1", "Nghệ thuật làm vườn và nhân giống cây hoa", "The art or practice of garden cultivation and management."),
    ("bonsai", "/ˈbɑːn.saɪ/", "noun", "B1", "Cây cảnh bonsai uốn thế độc đáo", "An ornamental tree or shrub grown in a pot and artificially prevented from reaching normal size."),
    ("knitting", "/ˈnɪt.ɪŋ/", "noun", "A2", "Đan len bằng que đan", "The craft or action of knitting clothing from yarn."),
    ("crochet", "/kroʊˈʃeɪ/", "noun", "B1", "Móc len bằng kim móc tạo hoa văn", "A handicraft in which yarn is made up into a textured fabric by means of a hooked needle."),
    ("quilting", "/ˈkwɪl.tɪŋ/", "noun", "B1", "Khâu ghép các mảnh vải chần bông thành chăn ấm", "The action of making quilts or stitching layers together."),
    ("scrapbooking", "/ˈskræpˌbʊk.ɪŋ/", "noun", "A2", "Làm sổ tay lưu niệm dán ảnh và hoa khô", "The activity of creating and maintaining a scrapbook as a hobby."),
    ("astrophotography", "/ˌæs.troʊ.fəˈtɑː.ɡrə.fi/", "noun", "B2", "Chụp ảnh thiên văn bầu trời đêm và dải ngân hà", "Photography of astronomical objects and celestial events."),
    ("birdwatching", "/ˈbɝːdˌwɑː.tʃɪŋ/", "noun", "A2", "Thú vui ngắm chim thiên nhiên qua ống nhòm", "The observation of birds in their natural environment as a hobby."),
    ("aquascaping", "/ˈæk.wəˌskeɪ.pɪŋ/", "noun", "B2", "Nghệ thuật bố cục thủy sinh trong bể kính", "The craft of arranging aquatic plants, rocks, stones, and driftwood in an aesthetically pleasing manner."),
    ("taxidermy", "/ˈtæk.sə.dɝː.mi/", "noun", "C1", "Nghệ thuật nhồi bông tiêu bản động vật", "The art of preparing, stuffing, and mounting the skins of animals with lifelike effect."),
    ("leathercraft", "/ˈleð.ɚ.kræft/", "noun", "B2", "Nghề thuộc da chế tác thủ công túi ví da", "The practice of making leather into craft objects or works of art."),
    ("macrame", "/ˌmæk.rəˈmeɪ/", "noun", "B1", "Nghệ thuật thắt nút dây trang trí treo chậu cây", "The art of knotting cord or string in patterns to make decorative articles."),
    ("candle-making", "/ˈkæn.dəl ˌmeɪ.kɪŋ/", "noun", "A2", "Tự đúc nến thơm nghệ thuật tại nhà", "The craft of making scented candles from soy wax or beeswax."),
    ("soapmaking", "/ˈsoʊpˌmeɪ.kɪŋ/", "noun", "B1", "Nấu xà phòng handmade từ dầu dừa thảo mộc", "The craft of creating natural artisanal soaps.")
])

# Topic 26: Weather, Seasons & Natural Disasters
add_terms("Weather, Seasons & Natural Disasters", [
    ("blizzard", "/ˈblɪz.ɚd/", "noun", "B1", "Trận bão tuyết mịt mù gió giật", "A severe snowstorm with high winds and low visibility."),
    ("avalanche", "/ˈæv.əl.æntʃ/", "noun", "B2", "Tuyết lở kinh hoàng ầm ầm từ đỉnh núi", "A mass of snow, ice, and rocks falling rapidly down a mountainside."),
    ("tsunami", "/tsuːˈnɑː.mi/", "noun", "B1", "Sóng thần đại dương khổng lồ sau động đất", "A long high sea wave caused by an earthquake or other disturbance."),
    ("earthquake", "/ˈɝːθ.kweɪk/", "noun", "A2", "Trận động đất rung chuyển mặt đất", "A sudden and violent shaking of the ground, sometimes causing great destruction."),
    ("richter scale", "/ˈrɪk.tɚ ˌskeɪl/", "noun", "B1", "Thang đo độ mạnh của động đất Richter", "A numerical scale for expressing the magnitude of an earthquake on the basis of seismograph oscillations."),
    ("epicenter", "/ˈep.ə.sen.t̬ɚ/", "noun", "B2", "Tâm chấn của trận động đất", "The point on the earth's surface vertically above the focus of an earthquake."),
    ("tornado", "/tɔːrˈneɪ.doʊ/", "noun", "B1", "Cơn lốc xoáy hình phễu cuốn phăng mọi thứ", "A mobile, destructive vortex of violently rotating winds having the appearance of a funnel-shaped cloud."),
    ("hurricane", "/ˈhɝː.ɪ.kən/", "noun", "B1", "Siêu bão nhiệt đới kèm cuồng phong dữ dội", "A storm with a violent wind, in particular a tropical cyclone in the Caribbean."),
    ("typhoon", "/taɪˈfuːn/", "noun", "B1", "Cơn bão nhiệt đới dữ dội ở vùng Tây Bắc Thái Bình Dương", "A tropical storm in the region of the Indian or western Pacific oceans."),
    ("mudslide", "/ˈmʌd.slaɪd/", "noun", "B1", "Vụ lở bùn đất cuốn trôi nhà cửa sau mưa lớn", "A mass of mud and other earthy material that is falling, or has fallen, down a hillside."),
    ("hailstorm", "/ˈheɪl.stɔːrm/", "noun", "B1", "Trận mưa đá lộp bộp từ trên trời rơi xuống", "A storm of heavy hail."),
    ("frostbite", "/ˈfrɑːst.baɪt/", "noun", "B2", "Bỏng lạnh hoại tử da do nhiệt độ quá thấp", "Injury to body tissues caused by exposure to extreme cold."),
    ("hypothermia", "/ˌhaɪ.poʊˈθɝː.mi.ə/", "noun", "B2", "Hạ thân nhiệt nguy hiểm tính mạng trong giá rét", "The condition of having an abnormally low body temperature, typically one that is dangerously low."),
    ("heatwave", "/ˈhiːt.weɪv/", "noun", "A2", "Đợt nắng nóng gay gắt kéo dài nhiều ngày", "A prolonged period of abnormally hot weather."),
    ("wildfire", "/ˈwaɪld.faɪr/", "noun", "B1", "Vụ cháy rừng bùng phát dữ dội khó khống chế", "A large, destructive fire that spreads quickly over woodland or brush."),
    ("downpour", "/ˈdaʊn.pɔːr/", "noun", "A2", "Cơn mưa rào như trút nước", "A heavy fall of rain."),
    ("barometer", "/bəˈrɑː.mə.t̬ɚ/", "noun", "B1", "Khí áp kế đo áp suất không khí dự báo thời tiết", "An instrument measuring atmospheric pressure, used especially in forecasting the weather."),
    ("anemometer", "/ˌæn.əˈmɑː.mə.t̬ɚ/", "noun", "B2", "phong kế đo tốc độ gió", "An instrument for measuring the speed of the wind, or of any current of gas."),
    ("humidity", "/hjuːˈmɪd.ə.t̬i/", "noun", "A2", "Độ ẩm của không khí", "The state or quality of being humid; a high amount of water vapor in the atmosphere."),
    ("meteorology", "/ˌmiː.t̬i.əˈrɑː.lə.dʒi/", "noun", "B2", "Ngành khí tượng học dự báo thời tiết", "The branch of science concerned with the processes and phenomena of the atmosphere, especially as a means of forecasting weather.")
])

print("[OK] Loaded domain expansion catalog modules.")
