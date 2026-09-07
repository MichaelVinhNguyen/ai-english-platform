"""
scripts/data/mega_final_reserve_bank.py
Master reserve of authentic domain terms for Topics 16 to 50.
Tuple: (word, ipa, pos, lvl, vi_def, en_def)
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

MEGA_RESERVE = {
    "Law, Crime & Justice": [
        ("bail", "/beɪl/", "noun", "B1", "Tiền bảo lãnh tại ngoại", "The temporary release of an accused person awaiting trial, sometimes on condition that a sum of money is lodged."),
        ("custody", "/ˈkʌs.tə.di/", "noun", "B2", "Sự tạm giam hoặc quyền giám hộ", "The protective care or guardianship of someone or something; imprisonment."),
        ("warrant", "/ˈwɔːr.ənt/", "noun", "B2", "Lệnh khám xét hoặc lệnh bắt giữ của tòa", "A document issued by a legal government official authorizing the police to make an arrest or search."),
        ("felon", "/ˈfel.ən/", "noun", "B2", "Kẻ phạm trọng tội đại hình", "A person who has been convicted of a felony."),
        ("clemency", "/ˈklem.ən.si/", "noun", "C1", "Sự khoan hồng giảm án của nguyên thủ", "Mercy; lenience shown by a ruler or judge toward an offender."),
        ("pardon", "/ˈpɑːr.dən/", "noun", "B2", "Lệnh ân xá tha bổng của tổng thống", "The action of forgiving or being forgiven for an error or offense; legal forgiveness."),
        ("inquest", "/ˈɪn.kwest/", "noun", "C1", "Cuộc điều tra tư pháp về cái chết bất thường", "A judicial inquiry to ascertain the facts relating to an incident, such as a sudden death."),
        ("verdict", "/ˈvɝː.dɪkt/", "noun", "B2", "Phán quyết cuối cùng của bồi thẩm đoàn", "A decision on a disputed issue in a civil or criminal case."),
        ("docket", "/ˈdɑː.kɪt/", "noun", "C1", "Lịch xét xử các vụ án của tòa", "A calendar or list of cases for trial or people having cases pending."),
        ("tribunal", "/traɪˈbjuː.nəl/", "noun", "B2", "Tòa án chuyên trách phân xử tranh chấp", "A court of justice or a seat or court of justice."),
        ("barrister", "/ˈber.ə.stɚ/", "noun", "B2", "Luật sư tranh tụng trước tòa án", "A lawyer entitled to practice as an advocate, particularly in the higher courts."),
        ("solicitor", "/səˈlɪs.ə.t̬ɚ/", "noun", "B2", "Luật sư tư vấn pháp lý và thảo hợp đồng", "A member of the legal profession qualified to deal with all matters of law and instruct barristers."),
        ("notary public", "/ˌnoʊ.t̬ɚ.i ˈpʌb.lɪk/", "noun", "B2", "Công chứng viên xác thực chữ ký giấy tờ", "A person authorized to perform certain legal formalities, especially to draw up or certify contracts."),
        ("alibi", "/ˈæl.ə.baɪ/", "noun", "B1", "Chứng cứ ngoại phạm không có mặt tại hiện trường", "A claim or piece of evidence that one was elsewhere when an act is alleged to have taken place."),
        ("extenuating", "/ɪkˈsten.ju.eɪ.t̬ɪŋ/", "adjective", "C1", "Tình tiết giảm nhẹ hình phạt", "Serving to lessen the seriousness of an offence."),
        ("aggravating", "/ˈæɡ.rə.veɪ.t̬ɪŋ/", "adjective", "C1", "Tình tiết tăng nặng hình phạt", "Making a problem or offence worse or more serious."),
        ("recidivism", "/rɪˈsɪd.ə.vɪ.zəm/", "noun", "C2", "Tỷ lệ tái phạm tội của người mãn hạn tù", "The tendency of a convicted criminal to reoffend."),
        ("rehabilitation", "/ˌriː.həˌbɪl.əˈteɪ.ʃən/", "noun", "B2", "Sự cải tạo hướng thiện cho phạm nhân", "The action of restoring someone to health or normal life through training and therapy after imprisonment."),
        ("penal code", "/ˈpiː.nəl ˌkoʊd/", "noun", "B2", "Bộ luật hình sự quốc gia", "A document which compiles all, or a significant amount of, a particular jurisdiction's criminal law."),
        ("subornation", "/ˌsʌb.ɔːrˈneɪ.ʃən/", "noun", "C2", "Tội mua chuộc nhân chứng khai man", "The crime of bribing or inducing someone to commit perjury."),
        ("litigant", "/ˈlɪt̬.ə.ɡənt/", "noun", "C1", "Đương sự tham gia tố tụng trong vụ án", "A person involved in a lawsuit."),
        ("jurisdiction", "/ˌdʒʊr.ɪsˈdɪk.ʃən/", "noun", "B2", "Thẩm quyền tài phán theo địa hạt", "The extent of the power to make legal decisions and judgments."),
        ("deposition", "/ˌdep.əˈzɪʃ.ən/", "noun", "C1", "Bản khai nhân chứng ngoài tòa án", "The process of giving sworn evidence."),
        ("settlement", "/ˈset̬.əl.mənt/", "noun", "B1", "Thỏa thuận hòa giải dàn xếp ngoài tòa", "An official agreement intended to resolve a dispute or conflict.")
    ],

    "Politics, Diplomacy & Global Affairs": [
        ("supranational", "/ˌsuː.prəˈnæʃ.ən.əl/", "adjective", "C1", "Siêu quốc gia vượt trên thẩm quyền một nước", "Having power or influence that transcends national boundaries or governments."),
        ("sovereign", "/ˈsɑːv.rən/", "adjective", "B2", "Có chủ quyền tối cao độc lập", "Possessing supreme or ultimate power."),
        ("diplomacy", "/dɪˈploʊ.mə.si/", "noun", "B1", "Nghệ thuật ngoại giao bang giao quốc tế", "The profession, activity, or skill of managing international relations."),
        ("embargo", "/ɪmˈbɑːr.ɡoʊ/", "noun", "B2", "Lệnh cấm vận thông thương buôn bán", "An official ban on trade or other commercial activity with a particular country."),
        ("summit", "/ˈsʌm.ɪt/", "noun", "B1", "Hội nghị thượng đỉnh các nguyên thủ quốc gia", "A meeting between heads of government."),
        ("demarche", "/deɪˈmɑːrʃ/", "noun", "C2", "Công hàm phản kháng ngoại giao chính thức", "A political step or initiative, especially in diplomatic affairs."),
        ("annex", "/əˈneks/", "verb", "C1", "Sáp nhập lãnh thổ bằng sức mạnh", "Append or add as an extra or subordinate part, especially to a country."),
        ("hegemon", "/ˈhedʒ.ə.mɑːn/", "noun", "C2", "Quốc gia bá chủ chi phối toàn cầu", "A supreme leader or dominant nation."),
        ("unipolar", "/ˌjuː.nəˈpoʊ.lɚ/", "adjective", "C1", "Thế giới đơn cực do một siêu cường thống trị", "Having or relating to a single pole or dominant power."),
        ("bipolar", "/baɪˈpoʊ.lɚ/", "adjective", "B2", "Thế giới lưỡng cực đối đầu như thời Chiến tranh Lạnh", "Having or relating to two opposite poles or dominant power blocs."),
        ("multilateral", "/ˌmʌl.tiˈlæt̬.ɚ.əl/", "adjective", "B2", "Đa phương có sự tham gia của nhiều nước", "Agreed upon or participated in by three or more parties."),
        ("armistice", "/ˈɑːr.mə.stɪs/", "noun", "C1", "Hiệp định đình chiến tạm ngừng giao tranh", "An agreement made by opposing sides in a war to stop fighting."),
        ("neutrality", "/nuːˈtræl.ə.t̬i/", "noun", "B2", "Chính sách trung lập không theo phe nào", "The state of not supporting or helping either side in a conflict."),
        ("non-aligned", "/ˌnɑːn.əˈlaɪnd/", "adjective", "C1", "Không liên kết không đứng về khối quân sự nào", "Not allied with any other nation or group of nations."),
        ("insurgency", "/ɪnˈsɝː.dʒən.si/", "noun", "C1", "Cuộc nổi dậy vũ trang chống chính quyền", "An active revolt or uprising."),
        ("containment", "/kənˈteɪn.mənt/", "noun", "C1", "Chiến lược bao vây kiềm chế thế lực thù địch", "The action of keeping something harmful under control or within limits."),
        ("geopolitics", "/ˌdʒiː.oʊˈpɑː.lə.tɪks/", "noun", "B2", "Địa chính trị toàn cầu", "Politics, especially international relations, as influenced by geographical factors."),
        ("treaty", "/ˈtriː.t̬i/", "noun", "B2", "Hiệp ước quốc tế có chữ ký cam kết", "A formally concluded and ratified agreement between states."),
        ("sanction", "/ˈsæŋk.ʃən/", "noun", "B2", "Lệnh trừng phạt kinh tế", "A threatened penalty for disobeying a law or rule."),
        ("referendum", "/ˌref.əˈren.dəm/", "noun", "B2", "Trưng cầu ý kiến toàn dân", "A general vote by the electorate on a single political question."),
        ("coalition", "/ˌkoʊ.əˈlɪʃ.ən/", "noun", "B2", "Liên minh chính phủ kết hợp", "A temporary alliance for combined action.")
    ],

    "Science, Space & Astronomy": [
        ("supernova", "/ˌsuː.pɚˈnoʊ.və/", "noun", "B2", "Vụ nổ siêu tân tinh giải phóng năng lượng lớn", "A star that suddenly increases greatly in brightness because of a catastrophic explosion."),
        ("astronomy", "/əˈstrɑː.nə.mi/", "noun", "A2", "Thiên văn học quan sát bầu trời", "The branch of science which deals with celestial objects, space, and the physical universe."),
        ("telescope", "/ˈtel.ə.skoʊp/", "noun", "A2", "Kính thiên văn ngắm sao xa", "An optical instrument designed to make distant objects appear nearer."),
        ("constellation", "/ˌkɑːn.stəˈleɪ.ʃən/", "noun", "B1", "Chòm sao tạo hình thù trên bầu trời đêm", "A group of stars forming a recognizable pattern that is traditionally named."),
        ("comet", "/ˈkɑː.mɪt/", "noun", "B1", "Sao chổi có dải đuôi bụi sáng rực", "A celestial object consisting of a nucleus of ice and dust and a trailing tail."),
        ("asteroid", "/ˈæs.tə.rɔɪd/", "noun", "B1", "Tiểu hành tinh đá trong hệ mặt trời", "A small rocky body orbiting the sun."),
        ("meteor", "/ˈmiː.t̬i.ɔːr/", "noun", "B1", "Sao băng lóe sáng khi bốc cháy trong khí quyển", "A small body of matter from outer space that enters the earth's atmosphere, becoming incandescent as a result of friction."),
        ("meteorite", "/ˈmiː.t̬i.ə.raɪt/", "noun", "B2", "Thiên thạch rơi xuống mặt đất", "A piece of rock or metal that has fallen to the earth's surface from outer space."),
        ("nebula", "/ˈneb.jə.lə/", "noun", "B2", "Tinh vân đám mây vũ trụ khổng lồ", "A cloud of gas and dust in outer space, visible in the night sky."),
        ("gravity", "/ˈɡræv.ə.t̬i/", "noun", "B1", "Lực hấp dẫn kéo vạn vật về tâm trái đất", "The force that attracts a body towards the center of the earth, or towards any other physical body having mass."),
        ("orbit", "/ˈɔːr.bɪt/", "noun", "B1", "Quỹ đạo quay quanh thiên thể", "The curved path of a celestial object or spacecraft round a star, planet, or moon."),
        ("satellite", "/ˈsæt̬.əl.aɪt/", "noun", "B1", "Vệ tinh nhân tạo hoặc vệ tinh tự nhiên", "An artificial body placed in orbit round the earth or moon or another planet in order to collect information."),
        ("eclipse", "/ɪˈklɪps/", "noun", "B1", "Nhật thực hoặc nguyệt thực che khuất", "An obscuring of the light from one celestial body by the passage of another between it and the spectator."),
        ("equinox", "/ˈek.wə.nɑːks/", "noun", "B2", "Ngày xuân phân thu phân ngày dài bằng đêm", "The time or date (twice each year) at which the sun crosses the celestial equator, when day and night are of equal length."),
        ("solstice", "/ˈsɑːl.stɪs/", "noun", "B2", "Ngày hạ chí đông chí ngày dài nhất hoặc ngắn nhất", "Either of the two times in the year, the summer solstice and the winter solstice, when the sun reaches its highest or lowest point in the sky."),
        ("black hole", "/ˈblæk ˌhoʊl/", "noun", "B1", "Hố đen lực hấp dẫn vô cực", "A region of space having a gravitational field so intense that no matter or radiation can escape."),
        ("galaxy", "/ˈɡæl.ək.si/", "noun", "B1", "Thiên hà chứa hàng trăm tỷ vì sao", "A system of millions or billions of stars, together with gas and dust, held together by gravitational attraction."),
        ("milky way", "/ˌmɪl.ki ˈweɪ/", "noun", "A2", "Dải Ngân Hà nơi hệ Mặt Trời cư ngụ", "The galaxy of which the solar system is a part."),
        ("light-year", "/ˈlaɪt.jɪr/", "noun", "B1", "Năm ánh sáng thước đo khoảng cách thiên văn", "A unit of astronomical distance equivalent to the distance that light travels in one year."),
        ("parsec", "/ˈpɑːr.sek/", "noun", "C1", "Parsec khoảng 3.26 năm ánh sáng", "A unit of distance used in astronomy, equal to about 3.26 light years."),
        ("observatory", "/əbˈzɝː.və.tɔːr.i/", "noun", "B2", "Đài quan sát thiên văn trên đỉnh núi", "A room or building housing an astronomical telescope or other scientific equipment for the study of natural phenomena."),
        ("cosmonaut", "/ˈkɑːz.mə.nɑːt/", "noun", "B1", "Nhà du hành vũ trụ", "A Russian astronaut."),
        ("astronaut", "/ˈæs.trə.nɑːt/", "noun", "A2", "Phi hành gia bay vào vũ trụ", "A person who is trained to travel in a spacecraft."),
        ("launchpad", "/ˈlɑːntʃ.pæd/", "noun", "B1", "Bệ phóng tên lửa vũ trụ", "An area on which a rocket or spacecraft sits prior to launch."),
        ("space station", "/ˈspeɪs ˌsteɪ.ʃən/", "noun", "A2", "Trạm vũ trụ quốc tế trên quỹ đạo", "A large artificial satellite used as a long-term base for human operations in space."),
        ("space shuttle", "/ˈspeɪs ˌʃʌt̬.əl/", "noun", "A2", "Tàu con thoi tái sử dụng nhiều lần", "A rocket-launched spacecraft, able to land like an unpowered aircraft, used to make repeated journeys between the earth and space."),
        ("deep space", "/ˌdiːp ˈspeɪs/", "noun", "B2", "Không gian sâu thẳm ngoài hệ mặt trời", "The region of space beyond the moon or beyond the solar system."),
        ("zenith", "/ˈzen.ɪθ/", "noun", "C1", "Thiên đỉnh điểm cao nhất thẳng đứng trên đầu", "The point in the sky or celestial sphere directly above an observer.")
    ],

    "Architecture, Housing & Real Estate": [
        ("cornice", "/ˈkɔːr.nɪs/", "noun", "C1", "Gờ chỉ phào trang trí mép trần nhà", "An ornamental molding around the wall of a room just below the ceiling."),
        ("cupola", "/ˈkjuː.pə.lə/", "noun", "C1", "Mái vòm tròn nhỏ trên đỉnh tháp nhà", "A small dome, especially a small dome on a drum on top of a larger dome."),
        ("pergola", "/ˈpɝː.ɡə.lə/", "noun", "B2", "Giàn hoa leo ngoài vườn râm mát", "An arched structure in a garden having a framework covered with climbing plants."),
        ("balustrade", "/ˈbæl.ə.streɪd/", "noun", "C1", "Dãy con tiện lan can cầu thang bằng đá", "A railing supported by balusters, especially one forming an ornamental parapet to a balcony."),
        ("skylight", "/ˈskaɪ.laɪt/", "noun", "B1", "Cửa sổ trần lấy sáng tự nhiên", "A window set in a roof or ceiling at the same angle."),
        ("parapet", "/ˈper.ə.pɪt/", "noun", "C1", "Tường bao quanh mép sân thượng an toàn", "A low protective wall along the edge of a roof, bridge, or balcony."),
        ("portico", "/ˈpɔːr.t̬ə.koʊ/", "noun", "C1", "Hiên sảnh lớn có hàng cột chống đỡ phong cách Hy Lạp", "A structure consisting of a roof supported by columns at regular intervals, typically attached for a porch to a building."),
        ("turret", "/ˈtɝː.ɪt/", "noun", "B2", "Tháp canh nhỏ nhô ra từ góc tường lâu đài", "A small tower on top of a larger tower or at the corner of a building or wall, typically of a castle."),
        ("gargoyle", "/ˈɡɑːr.ɡɔɪl/", "noun", "B2", "Tượng máng xối hình quái thú thời Gothic", "A carved human or animal face with a spout designed to carry water clear of a wall."),
        ("clerestory", "/ˈklɪr.stɔːr.i/", "noun", "C2", "Hàng cửa sổ kính thông gió sát mái nhà", "The upper part of the nave, choir, and transepts of a large church, containing a series of windows."),
        ("cantilever", "/ˈkæn.t̬əˌliː.vɚ/", "noun", "C1", "Dầm chìa nhô ra ngoài không cần cột chống", "A long projecting beam or girder fixed at only one end, used in bridge construction."),
        ("buttress", "/ˈbʌt.rəs/", "noun", "C1", "Trụ chống gia cố tường ngoài của nhà thờ đá", "A projecting support of stone or brick built against a wall."),
        ("alcove", "/ˈæl.koʊv/", "noun", "B2", "Hốc tường trang trí hoặc góc nghỉ ngơi", "A recess in the wall of a room or garden."),
        ("vestibule", "/ˈves.tə.bjuːl/", "noun", "C1", "Tiền sảnh đệm trước khi bước vào phòng khách", "An antechamber, hall, or lobby next to the outer door of a building."),
        ("mezzanine", "/ˈmez.ə.niːn/", "noun", "B2", "Tầng lửng giữa tầng trệt và lầu một", "A low story between two others in a building."),
        ("atrium", "/ˈeɪ.tri.əm/", "noun", "B2", "Khoảng giếng trời thông tầng thoáng đãng", "An open-roofed entrance hall or central court in an ancient Roman house, or modern open skylit central area."),
        ("basement", "/ˈbeɪs.mənt/", "noun", "A2", "Tầng hầm để xe hoặc trữ đồ", "The floor of a building which is partly or entirely below ground level."),
        ("attic", "/ˈæt̬.ɪk/", "noun", "A2", "Gác xép áp mái ấm cúng", "A space or room just below the roof of a building."),
        ("landlord", "/ˈlænd.lɔːrd/", "noun", "A2", "Chủ nhà cho thuê bất động sản", "A person, especially a man, who rents land, a building, or an apartment to a tenant."),
        ("tenant", "/ˈten.ənt/", "noun", "B1", "Người thuê nhà đóng tiền hàng tháng", "A person who occupies land or property rented from a landlord."),
        ("lease", "/liːs/", "noun", "B1", "Hợp đồng thuê nhà dài hạn", "A contract by which one party conveys land, property, services, etc. to another for a specified time."),
        ("sublet", "/ˈsʌb.let/", "verb", "B2", "Cho thuê lại phòng cho người thứ ba", "Lease a property to a subtenant."),
        ("eviction", "/ɪˈvɪk.ʃən/", "noun", "B2", "Sự trục xuất cưỡng chế người thuê vi phạm", "The action of expelling someone, especially a tenant, from a property."),
        ("mortgage", "/ˈmɔːr.ɡɪdʒ/", "noun", "B1", "Khoản vay thế chấp mua nhà ngân hàng", "A legal agreement by which a bank or other creditor lends money at interest in exchange for taking title of the debtor's property.")
    ]
}

print(f"MEGA_RESERVE loaded: {len(MEGA_RESERVE)} topics.")
