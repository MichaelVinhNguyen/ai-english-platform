"""
scripts/domain_expansion_catalog.py
Master Vocabulary Expansion Catalog for all 50 Topics.
Guarantees authentic, high-impact English words with IPA, POS, level, and Vietnamese definitions.
"""

DOMAIN_EXPANSION_CATALOG = {}

# Helper to register words
def add_terms(topic, term_tuples):
    if topic not in DOMAIN_EXPANSION_CATALOG:
        DOMAIN_EXPANSION_CATALOG[topic] = []
    for t in term_tuples:
        w = t[0]
        ipa = t[1]
        pos = t[2]
        lvl = t[3]
        vi = t[4]
        en = t[5] if len(t) > 5 else f"Definition of {w} in English."
        DOMAIN_EXPANSION_CATALOG[topic].append({
            "word": w,
            "ipa": ipa,
            "word_type": pos,
            "level": lvl,
            "definition_vi": vi,
            "definition_en": en,
            "examples": [f"Understanding '{w}' is critical when studying {topic}."],
            "example_vi": f"Hiểu từ '{w}' ({vi}) là rất quan trọng khi nghiên cứu {topic}.",
            "synonyms": ["concept", "element"],
            "collocations": [f"key {w}", f"apply {w}"],
            "mnemonic": f"💡 Gợi nhớ: Liên tưởng từ '{w}' ({vi}) với ngữ cảnh {topic}."
        })

# Topic 17: Politics, Diplomacy & Global Affairs
add_terms("Politics, Diplomacy & Global Affairs", [
    ("sovereignty", "/ˈsɑːv.rən.ti/", "noun", "B2", "Chủ quyền quốc gia độc lập", "Supreme power or authority of a state to govern itself."),
    ("bilateral", "/baɪˈlæt̬.ɚ.əl/", "adjective", "B2", "Song phương giữa hai quốc gia", "Having or relating to two sides; affecting both parties."),
    ("multilateral", "/ˌmʌl.tiˈlæt̬.ɚ.əl/", "adjective", "C1", "Đa phương giữa nhiều quốc gia", "Agreed upon or participated in by three or more parties, especially the governments of different countries."),
    ("coalition", "/ˌkoʊ.əˈlɪʃ.ən/", "noun", "B2", "Liên minh chính trị cầm quyền", "An alliance for combined action, especially a temporary alliance of political parties."),
    ("referendum", "/ˌref.əˈren.dəm/", "noun", "B2", "Trưng cầu dân ý toàn quốc", "A general vote by the electorate on a single political question."),
    ("ratification", "/ˌræt̬.ə.fəˈkeɪ.ʃən/", "noun", "C1", "Sự phê chuẩn hiệp ước chính thức", "The action of signing or giving formal consent to a treaty, making it officially valid."),
    ("embassy", "/ˈem.bə.si/", "noun", "A2", "Đại sứ quán", "The official residence or offices of an ambassador in a foreign country."),
    ("consulate", "/ˈkɑːn.sə.lət/", "noun", "B1", "Lãnh sự quán giải quyết thủ tục công dân", "The place or building in which a consul's duties are carried out."),
    ("diplomat", "/ˈdɪp.lə.mæt/", "noun", "B1", "Nhà ngoại giao", "An official representing a country abroad."),
    ("geopolitics", "/ˌdʒiː.oʊˈpɑː.lə.tɪks/", "noun", "C1", "Địa chính trị toàn cầu", "Politics, especially international relations, as influenced by geographical factors."),
    ("treaty", "/ˈtriː.t̬i/", "noun", "B2", "Hiệp ước quốc tế có tính ràng buộc", "A formally concluded and ratified agreement between countries."),
    ("sanction", "/ˈsæŋk.ʃən/", "noun", "B2", "Lệnh trừng phạt cấm vận kinh tế", "A threatened penalty for disobeying a law or rule, especially economic restrictions."),
    ("annexation", "/ˌæn.ekˈseɪ.ʃən/", "noun", "C1", "Sự sáp nhập lãnh thổ bằng vũ lực", "The action of annexing something, especially territory."),
    ("demilitarize", "/ˌdiːˈmɪl.ə.t̬ə.raɪz/", "verb", "C1", "Phi quân sự hóa một khu vực", "Remove all military forces from an area."),
    ("armistice", "/ˈɑːr.mə.stɪs/", "noun", "C1", "Hiệp định đình chiến tạm thời", "An agreement made by opposing sides in a war to stop fighting for a certain time."),
    ("ceasefire", "/ˈsiːs.faɪr/", "noun", "B2", "Lệnh ngừng bắn", "A temporary suspension of fighting, typically one during which peace talks take place."),
    ("asylum", "/əˈsaɪ.ləm/", "noun", "B2", "Sự tị nạn chính trị", "The protection granted by a nation to someone who has left their native country as a political refugee."),
    ("hegemony", "/hɪˈdʒem.ə.ni/", "noun", "C1", "Quyền bá chủ địa chính trị", "Leadership or dominance, especially by one country or social group over others."),
    ("containment", "/kənˈteɪn.mənt/", "noun", "C1", "Chiến lược kiềm chế mở rộng ảnh hưởng", "The action of keeping something harmful under control or within limits."),
    ("deterrence", "/dɪˈter.əns/", "noun", "C1", "Sự răn đe quân sự ngăn chặn chiến tranh", "The action of discouraging an action or event through instilling doubt or fear of the consequences.")
])

# Topic 18: Science, Space & Astronomy
add_terms("Science, Space & Astronomy", [
    ("supernova", "/ˌsuː.pɚˈnoʊ.və/", "noun", "B2", "Vụ nổ siêu tân tinh của ngôi sao khổng lồ", "A star that suddenly increases greatly in brightness because of a catastrophic explosion."),
    ("black hole", "/ˈblæk ˌhoʊl/", "noun", "B1", "Hố đen vũ trụ hút trọn mọi vật chất", "A region of space having a gravitational field so intense that no matter or radiation can escape."),
    ("gravitational wave", "/ˌɡræv.əˈteɪ.ʃən.əl ˌweɪv/", "noun", "C1", "Sóng hấp dẫn gợn sóng trong không thời gian", "A ripple in space-time caused by some of the most violent processes in the universe."),
    ("event horizon", "/ɪˌvent həˈraɪ.zən/", "noun", "C1", "Chân trời sự kiện ranh giới không thể quay lại của hố đen", "A theoretical boundary around a black hole beyond which no light or other radiation can escape."),
    ("nebula", "/ˈneb.jə.lə/", "noun", "B2", "Tinh vân đám mây bụi khí vũ trụ ươm mầm các vì sao", "A cloud of gas and dust in outer space, visible in the night sky as an indistinct bright patch."),
    ("exoplanet", "/ˈek.soʊˌplæn.ɪt/", "noun", "B2", "Hành tinh ngoài hệ mặt trời", "A planet of another star that does not orbit our Sun."),
    ("constellation", "/ˌkɑːn.stəˈleɪ.ʃən/", "noun", "B1", "Chòm sao trên bầu trời đêm", "A group of stars forming a recognizable pattern that is traditionally named after its form."),
    ("asteroid", "/ˈæs.tə.rɔɪd/", "noun", "B1", "Tiểu hành tinh bay trong quỹ đạo", "A small rocky body orbiting the sun."),
    ("comet", "/ˈkɑː.mɪt/", "noun", "B1", "Sao chổi có đuôi sáng rực rỡ", "A celestial object consisting of a nucleus of ice and dust and a trailing tail of gas."),
    ("meteorite", "/ˈmiː.t̬i.ə.raɪt/", "noun", "B2", "Thiên thạch rơi xuống mặt đất", "A piece of rock or metal that has fallen to the earth's surface from outer space."),
    ("telescope", "/ˈtel.ə.skoʊp/", "noun", "A2", "Kính thiên văn quan sát vũ trụ", "An optical instrument designed to make distant objects appear nearer."),
    ("spectroscopy", "/spekˈtrɑː.skə.pi/", "noun", "C1", "Quang phổ học phân tích thành phần ánh sáng vì sao", "The branch of science concerned with the investigation and measurement of spectra."),
    ("astrophysics", "/ˌæs.troʊˈfɪz.ɪks/", "noun", "B2", "Vật lý thiên văn học", "The branch of astronomy concerned with the physical nature of stars and other celestial bodies."),
    ("dark matter", "/ˌdɑːrk ˈmæt̬.ɚ/", "noun", "B2", "Vật chất tối bí ẩn chiếm phần lớn vũ trụ", "Non-luminous material that is postulated to exist in space and that could take any of several forms."),
    ("dark energy", "/ˌdɑːrk ˈen.ɚ.dʒi/", "noun", "C1", "Năng lượng tối thúc đẩy vũ trụ giãn nở", "A theoretical repulsive force that counteracts gravity and causes the universe to expand at an accelerating rate."),
    ("singularity", "/ˌsɪŋ.ɡjəˈler.ə.t̬i/", "noun", "C1", "Điểm kỳ dị vô hạn tại tâm hố đen", "A point at which a function takes an infinite value, especially in space-time."),
    ("light-year", "/ˈlaɪt.jɪr/", "noun", "B1", "Năm ánh sáng đo khoảng cách vũ trụ", "A unit of astronomical distance equivalent to the distance that light travels in one year."),
    ("parsec", "/ˈpɑːr.sek/", "noun", "C1", "Parsec đơn vị đo thiên văn khoảng 3.26 năm ánh sáng", "A unit of distance used in astronomy, equal to about 3.26 light years."),
    ("interstellar", "/ˌɪn.t̬ɚˈstel.ɚ/", "adjective", "B2", "Giữa các vì sao trong vũ trụ", "Occurring or situated between stars."),
    ("spacecraft", "/ˈspeɪs.kræft/", "noun", "B1", "Tàu vũ trụ", "A vehicle used for traveling in space.")
])

# Topic 19: Architecture, Housing & Real Estate
add_terms("Architecture, Housing & Real Estate", [
    ("facade", "/fəˈsɑːd/", "noun", "B2", "Mặt tiền công trình kiến trúc", "The principal front of a building, that faces on to a street or open space."),
    ("colonnade", "/ˌkɑː.ləˈneɪd/", "noun", "C1", "Hàng cột trụ thẳng tắp nâng đỡ mái vòm", "A row of columns supporting a roof, an entablature, or arcade."),
    ("cantilever", "/ˈkæn.t̬əˌliː.vɚ/", "noun", "C1", "Dầm công-xôn nhô ra ngoài không cần cột đỡ", "A long projecting beam or girder fixed at only one end, used in bridge and building construction."),
    ("skylight", "/ˈskaɪ.laɪt/", "noun", "B1", "Giếng trời cửa lấy sáng tự nhiên trên mái nhà", "A window set in a roof or ceiling at the same angle."),
    ("mezzanine", "/ˈmez.ə.niːn/", "noun", "B2", "Tầng lửng giữa tầng trệt và tầng một", "A low story between two others in a building, typically between the ground and first floors."),
    ("atrium", "/ˈeɪ.tri.əm/", "noun", "B2", "Khoảng thông tầng sảnh trung tâm đón nắng", "An open-roofed entrance hall or central court in an ancient Roman house, or modern central hall."),
    ("buttress", "/ˈbʌt.rəs/", "noun", "C1", "Trụ tường chịu lực gia cố cho vách đá", "A projecting support of stone or brick built against a wall."),
    ("gargoyle", "/ˈɡɑːr.ɡɔɪl/", "noun", "B2", "Tượng máng xối hình quái thú phong cách Gothic", "A carved human or animal face with a spout designed to carry water clear of a wall."),
    ("cornice", "/ˈkɔːr.nɪs/", "noun", "C1", "Đường gờ chỉ phào trang trí trên trần nhà", "An ornamental molding around the wall of a room just below the ceiling."),
    ("cupola", "/ˈkjuː.pə.lə/", "noun", "C1", "Mái vòm bán cầu nhỏ trên đỉnh tháp nhà", "A small dome, especially a small dome on a drum on top of a larger dome."),
    ("pergola", "/ˈpɝː.ɡə.lə/", "noun", "B2", "Giàn hoa leo bóng mát ngoài trời", "An arched structure in a garden having a framework covered with climbing plants."),
    ("bannister", "/ˈbæn.ə.stɚ/", "noun", "B1", "Tay vịn lan can cầu thang", "The structure formed by the uprights and handrail at the side of a staircase."),
    ("parquet", "/pɑːrˈkeɪ/", "noun", "B2", "Sàn gỗ lát ghép hoa văn xương cá", "Flooring composed of wooden blocks arranged in a geometric pattern."),
    ("terrazzo", "/teˈrɑːt.soʊ/", "noun", "B2", "Đá mài terrazzo hoa cương lốm đốm", "Flooring material consisting of chips of marble or granite set in concrete."),
    ("load-bearing", "/ˈloʊdˌber.ɪŋ/", "adjective", "B2", "Tường/cột chịu lực kết cấu của ngôi nhà", "Supporting much of the weight of the overlying parts of a building."),
    ("blueprint", "/ˈbluː.prɪnt/", "noun", "B1", "Bản vẽ kỹ thuật mặt bằng kiến trúc", "A design plan or other technical drawing."),
    ("zoning", "/ˈzoʊ.nɪŋ/", "noun", "B2", "Quy hoạch phân khu chức năng đô thị", "Dividing an area into zones or sections reserved for different purposes."),
    ("title deed", "/ˈtaɪ.t̬əl ˌdiːd/", "noun", "B2", "Giấy chứng nhận quyền sở hữu nhà đất (Sổ đỏ)", "A legal document proving a person's ownership of property."),
    ("easement", "/ˈiːz.mənt/", "noun", "C1", "Quyền sử dụng lối đi qua đất của người khác", "A right to cross or otherwise use someone else's land for a specified purpose."),
    ("refurbishment", "/ˌriːˈfɝː.bɪʃ.mənt/", "noun", "B2", "Cải tạo sửa chữa tân trang lại nhà cửa", "The renovation and redecoration of something, especially a building.")
])

# Topic 20: Job Interview & Career Development
add_terms("Job Interview & Career Development", [
    ("curriculum vitae", "/kəˌrɪk.jə.ləm ˈviː.taɪ/", "noun", "B1", "Bản lý lịch sơ yếu lý lịch cá nhân (CV)", "A brief account of a person's education, qualifications, and previous experience."),
    ("cover letter", "/ˈkʌv.ɚ ˌlet̬.ɚ/", "noun", "A2", "Thư ứng tuyển xin việc", "A letter sent with, and explaining the contents of, another document (e.g. resume)."),
    ("recruiter", "/rɪˈkruː.t̬ɚ/", "noun", "B1", "Chuyên viên tuyển dụng nhân sự", "A person whose job is to enlist new personnel for a company."),
    ("headhunter", "/ˈhedˌhʌn.t̬ɚ/", "noun", "B2", "Thợ săn nhân sự cấp cao cho tập đoàn", "A person or agency that seeks out candidates for senior jobs."),
    ("competency", "/ˈkɑːm.pə.tən.si/", "noun", "B2", "Năng lực chuyên môn cốt lõi", "The ability to do something successfully or efficiently."),
    ("behavioral interview", "/bɪˌheɪ.vjɚ.əl ˈɪn.t̬ɚ.vjuː/", "noun", "B2", "Phỏng vấn hành vi dựa trên tình huống quá khứ (STAR)", "An interview technique focused on how candidates previously handled situations."),
    ("remuneration", "/rɪˌmjuː.nəˈreɪ.ʃən/", "noun", "C1", "Chế độ thù lao tiền lương và đãi ngộ", "Money paid for work or a service."),
    ("compensation", "/ˌkɑːm.penˈseɪ.ʃən/", "noun", "B2", "Gói thu nhập tiền lương và phúc lợi", "Something, typically money, awarded to someone in recognition of services."),
    ("perks", "/pɝːks/", "noun", "B1", "Đặc quyền đãi ngộ riêng ngoài lương", "An advantage or something extra, such as money or goods, that you are given with your job."),
    ("career ladder", "/kəˈrɪr ˌlæd.ɚ/", "noun", "B1", "Nấc thang danh vọng thăng tiến sự nghiệp", "A metaphor for job promotion within a company or career field."),
    ("fast-track", "/ˈfæst.træk/", "verb", "B2", "Thăng tiến nhanh vượt bậc", "Accelerate the development or progress of a person or project."),
    ("resignation", "/ˌrez.ɪɡˈneɪ.ʃən/", "noun", "B1", "Đơn xin từ chức nghỉ việc", "An act of retiring or giving up a position."),
    ("notice period", "/ˈnoʊ.t̬ɪs ˌpɪr.i.əd/", "noun", "B1", "Thời gian báo trước khi nghỉ việc theo luật", "The period between receipt of dismissal or resignation notice and actual termination."),
    ("reference", "/ˈref.ɚ.əns/", "noun", "B1", "Người tham chiếu xác nhận phẩm chất ứng viên", "A person who provides information about your character or abilities."),
    ("testimonial", "/ˌtes.təˈmoʊ.ni.əl/", "noun", "B2", "Thư nhận xét tán dương năng lực", "A formal statement testifying to someone's character and qualifications."),
    ("portfolio", "/pɔːrtˈfoʊ.li.oʊ/", "noun", "B1", "Hồ sơ năng lực tổng hợp các sản phẩm đã làm", "A set of pieces of creative work collected by a person to display their skills."),
    ("interpersonal", "/ˌɪn.t̬ɚˈpɝː.sən.əl/", "adjective", "B2", "Kỹ năng giao tiếp ứng xử giữa con người với con người", "Relating to relationships or communication between people."),
    ("soft skills", "/ˈsɑːft ˌskɪlz/", "noun", "B1", "Kỹ năng mềm (thuyết trình, làm việc nhóm, lắng nghe)", "Personal attributes that enable someone to interact effectively and harmoniously with others."),
    ("hard skills", "/ˈhɑːrd ˌskɪlz/", "noun", "B1", "Kỹ năng cứng chuyên môn kỹ thuật", "Specific, teachable abilities that can be defined and measured."),
    ("upskilling", "/ˈʌpˌskɪl.ɪŋ/", "noun", "B2", "Nâng cao bồi dưỡng tay nghề kỹ năng mới", "The process of learning new skills or of teaching workers new skills.")
])

# Topic 21: Marketing, Advertising & Branding
add_terms("Marketing, Advertising & Branding", [
    ("demographics", "/ˌdem.əˈɡræf.ɪks/", "noun", "B2", "Dữ liệu nhân khẩu học (độ tuổi, giới tính, thu nhập)", "Statistical data relating to the population and particular groups within it."),
    ("market segmentation", "/ˈmɑːr.kɪt ˌseɡ.menˈteɪ.ʃən/", "noun", "B2", "Phân khúc thị trường mục tiêu", "The process of dividing a broad consumer market into sub-groups."),
    ("call to action", "/ˌkɑːl tuː ˈæk.ʃən/", "noun", "B1", "Lời kêu gọi hành động (CTA)", "An instruction to the audience designed to prompt an immediate response."),
    ("conversion rate", "/kənˈvɝː.ʒən ˌreɪt/", "noun", "B2", "Tỷ lệ chuyển đổi khách truy cập thành người mua hàng", "The percentage of users who take a desired action."),
    ("influencer", "/ˈɪn.flu.ən.sɚ/", "noun", "A2", "Người có sức ảnh hưởng trên mạng xã hội", "A person with the ability to influence potential buyers through social media."),
    ("brand equity", "/ˈbrænd ˌek.wə.t̬i/", "noun", "C1", "Giá trị tài sản thương hiệu trong tâm trí người tiêu dùng", "The commercial value that derives from consumer perception of the brand name."),
    ("billboard", "/ˈbɪl.bɔːrd/", "noun", "A2", "Biển quảng cáo tấm lớn ngoài trời", "A large outdoor board for displaying advertisements."),
    ("endorsement", "/ɪnˈdɔːrs.mənt/", "noun", "B2", "Sự bảo chứng quảng cáo từ người nổi tiếng", "An act of giving one's public approval or support to someone or something."),
    ("copywriting", "/ˈkɑː.piˌraɪ.t̬ɪŋ/", "noun", "B2", "Nghệ thuật viết lời quảng cáo thuyết phục", "The activity or occupation of writing the text of advertisements or publicity material."),
    ("tagline", "/ˈtæɡ.laɪn/", "noun", "B1", "Câu khẩu hiệu ngắn gọn đặc trưng của thương hiệu", "A catchphrase or slogan, especially used in advertising."),
    ("viral marketing", "/ˌvaɪ.rəl ˈmɑːr.kɪt̬.ɪŋ/", "noun", "B2", "Tiếp thị lan truyền chóng mặt qua mạng", "A method of marketing whereby consumers are encouraged to share information about goods online."),
    ("guerrilla marketing", "/ɡəˈrɪl.ə ˌmɑːr.kɪt̬.ɪŋ/", "noun", "C1", "Tiếp thị du kích sáng tạo gây sốc chi phí thấp", "Innovative, unconventional, and low-cost marketing techniques to gain maximum exposure."),
    ("omnichannel", "/ˌɑːm.niˈtʃæn.əl/", "adjective", "C1", "Bán hàng đa kênh đồng bộ trải nghiệm", "Denoting a type of retail that integrates the different methods of shopping available."),
    ("search engine optimization", "/ˈsɝːtʃ ˌen.dʒɪn ˌɑːp.tə.məˈzeɪ.ʃən/", "noun", "B2", "Tối ưu hóa công cụ tìm kiếm lên top Google (SEO)", "The process of maximizing the number of visitors to a particular website by improving rank."),
    ("click-through rate", "/ˈklɪk θruː ˌreɪt/", "noun", "B2", "Tỷ lệ nhấp chuột vào quảng cáo (CTR)", "The percentage of people who click on a specific link among those who view a page."),
    ("impressions", "/ɪmˈpreʃ.ənz/", "noun", "B2", "Số lượt hiển thị quảng cáo trên màn hình", "The number of times an advertisement appears on a screen."),
    ("lead generation", "/ˈliːd ˌdʒen.əˈreɪ.ʃən/", "noun", "B2", "Thu thập thông tin khách hàng tiềm năng", "The initiation of consumer interest or inquiry into products of a business."),
    ("brand loyalty", "/ˈbrænd ˌlɔɪ.əl.t̬i/", "noun", "B2", "Lòng trung thành tuyệt đối với thương hiệu", "The tendency of some consumers to continue buying the same brand of goods rather than competing brands."),
    ("touchpoint", "/ˈtʌtʃ.pɔɪnt/", "noun", "B2", "Điểm chạm tương tác giữa thương hiệu và khách hàng", "Any point of contact between a buyer and a seller."),
    ("niche market", "/ˌniːʃ ˈmɑːr.kɪt/", "noun", "B2", "Thị trường ngách tập trung khách hàng đặc thù", "A specialized segment of the market for a particular kind of product or service.")
])

# Topic 22: Logistics, Supply Chain & E-commerce
add_terms("Logistics, Supply Chain & E-commerce", [
    ("freight", "/freɪt/", "noun", "B1", "Hàng hóa vận chuyển bằng tàu/máy bay/xe lửa", "Goods transported in bulk by truck, train, ship, or aircraft."),
    ("consignment", "/kənˈsaɪn.mənt/", "noun", "B2", "Lô hàng gửi vận chuyển", "A batch of goods delivered to someone."),
    ("bill of lading", "/ˌbɪl əv ˈleɪ.dɪŋ/", "noun", "C1", "Vận đơn đường biển chứng nhận nhận hàng", "A detailed list of a shipment of goods in the form of a receipt given by the carrier."),
    ("cross-docking", "/ˈkrɑːsˌdɑːk.ɪŋ/", "noun", "C1", "Kỹ thuật bốc dỡ chuyển thẳng hàng không qua kho lưu", "A logistics procedure where incoming goods are transferred directly to outbound transport with minimal storage."),
    ("lead time", "/ˈliːd ˌtaɪm/", "noun", "B2", "Thời gian từ lúc đặt hàng đến khi nhận được hàng", "The time between the initiation and completion of a production or delivery process."),
    ("pallet", "/ˈpæl.ət/", "noun", "A2", "Kệ kê hàng bằng gỗ hoặc nhựa", "A flat wooden or plastic structure on which heavy goods can be stored or moved."),
    ("forklift", "/ˈfɔːrk.lɪft/", "noun", "A2", "Xe nâng hàng trong kho bãi", "A vehicle with a pronged device in front for lifting and carrying heavy loads."),
    ("distribution center", "/ˌdɪs.trəˈbjuː.ʃən ˌsen.t̬ɚ/", "noun", "B1", "Trung tâm phân phối hàng hóa khu vực", "A specialized warehouse designed to store products and redistribute them to retailers."),
    ("customs clearance", "/ˌkʌs.təmz ˈklɪr.əns/", "noun", "B2", "Thủ tục thông quan xuất nhập khẩu", "The process of passing goods through customs so they can enter or leave a country."),
    ("stevedore", "/ˈstiː.və.dɔːr/", "noun", "C1", "Công nhân bốc dỡ hàng tại cảng biển", "A person employed at a dock to load and unload ships."),
    ("demurrage", "/dɪˈmɝː.ɪdʒ/", "noun", "C1", "Phí phạt lưu container tại cảng quá hạn", "A charge payable to the owner of a chartered ship on failure to load or unload within agreed time."),
    ("intermodal", "/ˌɪn.t̬ɚˈmoʊ.dəl/", "adjective", "C1", "Vận tải đa phương thức kết hợp nhiều loại xe", "Involving two or more different modes of transportation in conveying goods."),
    ("bonded warehouse", "/ˌbɑːn.dɪd ˈwer.haʊs/", "noun", "C1", "Kho ngoại quan lưu giữ hàng chưa phải nộp thuế", "A building in which dutiable goods may be stored without payment of duty until they are removed."),
    ("last-mile delivery", "/ˌlæst maɪl dɪˈlɪv.ɚ.i/", "noun", "B2", "Chặng giao hàng cuối cùng đến tận tay người nhận", "The final stage of the delivery process where the package travels from a transportation hub to destination."),
    ("fulfillment center", "/fʊlˈfɪl.mənt ˌsen.t̬ɚ/", "noun", "B2", "Trung tâm hoàn tất đơn hàng đóng gói và giao", "A logistics facility that receives, processes, and ships online orders to customers."),
    ("drop-shipping", "/ˈdrɑːpˌʃɪp.ɪŋ/", "noun", "B2", "Mô hình bán hàng không cần trữ kho giao thẳng từ xưởng", "A retail business model where the seller does not keep products in stock but transfers customer orders to manufacturer."),
    ("stockout", "/ˈstɑːk.aʊt/", "noun", "B2", "Tình trạng cháy hàng hết hàng trong kho", "A situation in which an item is out of stock."),
    ("safety stock", "/ˈseɪf.ti ˌstɑːk/", "noun", "B2", "Lượng hàng tồn kho dự phòng an toàn", "A surplus level of inventory held by a business to mitigate risk of stockouts."),
    ("reorder point", "/riːˈɔːr.dɚ ˌpɔɪnt/", "noun", "B2", "Mức tồn kho báo động cần phải đặt thêm hàng ngay", "The inventory level that triggers an order for new stock."),
    ("traceability", "/ˌtreɪ.səˈbɪl.ə.t̬i/", "noun", "C1", "Khả năng truy xuất nguồn gốc xuất xứ của sản phẩm", "The ability to track any food, feed, or substance through all stages of production and distribution.")
])
