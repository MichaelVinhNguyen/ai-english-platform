"""
scripts/data/lexicon_filler_tier1.py
Exact authentic top-ups to complete Topics 2 to 32 to 100 words each.
"""

import sys
if sys.stdout.encoding != 'utf-8':
    try: sys.stdout.reconfigure(encoding='utf-8')
    except Exception: pass

FILLER_TIER1 = {
    "Food, Cooking & Dining": [
        ("confectionery", "/kənˈfek.ʃən.er.i/", "noun", "B2", "Bánh kẹo đồ ngọt cao cấp", "Sweets and chocolates collectively."),
        ("gastronomy", "/ɡæsˈtrɑː.nə.mi/", "noun", "B2", "Nghệ thuật ẩm thực sành điệu", "The practice or art of choosing, cooking, and eating good food.")
    ],
    "Travel, Tourism & Transportation": [
        ("wayfarer", "/ˈweɪˌfer.ɚ/", "noun", "C1", "Lữ khách lãng du bộ hành", "A person who travels on foot."),
        ("globetrotter", "/ˈɡloʊbˌtrɑː.t̬ɚ/", "noun", "B2", "Người đi du lịch khắp năm châu bốn biển", "A person who travels widely through many countries.")
    ],
    "Business, Management & Workplace": [
        ("delegation", "/ˌdel.əˈɡeɪ.ʃən/", "noun", "B2", "Sự ủy thác giao quyền cho cấp dưới", "The assignment of responsibility or authority to another person."),
        ("empowerment", "/ɪmˈpaʊ.ɚ.mənt/", "noun", "B2", "Sự trao quyền tự chủ cho nhân viên", "The process of becoming stronger and more confident, especially in controlling one's life and claiming one's rights.")
    ],
    "Education & Academic Life": [
        ("erudite", "/ˈer.jə.daɪt/", "adjective", "C1", "Uyên bác học rộng tài cao", "Having or showing great knowledge or learning.")
    ],
    "Shopping, Fashion & Retail": [
        ("prêt-à-porter", "/ˌpret.ɑː.pɔːrˈteɪ/", "noun", "C1", "Thời trang may sẵn cao cấp may hàng loạt theo size chuẩn", "Designer clothes sold in standard sizes rather than made to measure.")
    ],
    "Emotions, Personality & Character": [
        ("magnanimous", "/mæɡˈnæn.ə.məs/", "adjective", "C1", "Hào hiệp bao dung độ lượng", "Generous or forgiving, especially toward a rival or less powerful person."),
        ("tenacious", "/təˈneɪ.ʃəs/", "adjective", "B2", "Bền bỉ kiên trì không buông xuôi", "Tending to keep a firm hold of something; clinging closely; persistent."),
        ("vindictive", "/vɪnˈdɪk.tɪv/", "adjective", "C1", "Thù dai nuôi ý định trả thù", "Having or showing a strong or unreasoning desire for revenge."),
        ("affable", "/ˈæf.ə.bəl/", "adjective", "B2", "Niềm nở dễ gần thân thiện", "Friendly, good-natured, or easy to talk to."),
        ("gullible", "/ˈɡʌl.ə.bəl/", "adjective", "B2", "Cả tin dễ bị lừa gạt", "Easily persuaded to believe something; credulous."),
        ("pugnacious", "/pʌɡˈneɪ.ʃəs/", "adjective", "C1", "Hiếu chiến thích gây sự cãi cọ", "Eager or quick to argue, quarrel, or fight."),
        ("scrupulous", "/ˈskruː.pjə.ləs/", "adjective", "C1", "Cực kỳ liêm khiết tỉ mỉ đúng lương tâm", "Diligent, thorough, and extremely attentive to details or moral standards."),
        ("temperamental", "/ˌtem.prəˈmen.t̬əl/", "adjective", "B2", "Tính khí thất thường sáng nắng chiều mưa", "Liable to unreasonable changes of mood; erratic."),
        ("voracious", "/vəˈreɪ.ʃəs/", "adjective", "B2", "Háu ăn hoặc ngấu nghiến sách vở tri thức", "Wanting or devouring great quantities of food or information."),
        ("lucid", "/ˈluː.sɪd/", "adjective", "B2", "Minh mẫn diễn đạt rõ ràng rành mạch", "Expressed clearly; easy to understand; showing clarity of thought."),
        ("indolent", "/ˈɪn.dəl.ənt/", "adjective", "C1", "Lười biếng trốn tránh lao động", "Wanting to avoid activity or exertion; lazy.")
    ],
    "Family, Relationships & Society": [
        ("matrimonial", "/ˌmæt.rəˈmoʊ.ni.əl/", "adjective", "B2", "Thuộc về hôn nhân đời sống vợ chồng", "Relating to marriage or married people."),
        ("clan", "/klæn/", "noun", "B1", "Gia tộc dòng họ gắn bó", "A group of close-knit and interrelated families."),
        ("offspring", "/ˈɑːf.sprɪŋ/", "noun", "B1", "Con cái thế hệ sau trong gia đình", "A person's child or children."),
        ("hereditary", "/həˈred.ə.ter.i/", "adjective", "B2", "Di truyền thừa kế từ cha ông", "Conferred by or based on inheritance."),
        ("communal", "/kəˈmjuː.nəl/", "adjective", "B2", "Thuộc về cộng đồng chung", "Shared by all members of a community; for common use."),
        ("civic", "/ˈsɪv.ɪk/", "adjective", "B2", "Thuộc về bổn phận công dân đối với xã hội", "Relating to a city, town, or citizen duties."),
        ("cohabitation", "/ˌkoʊ.hæb.əˈteɪ.ʃən/", "noun", "B2", "Sống thử cùng nhau dưới một mái nhà", "The state of living together without marriage."),
        ("upbringing", "/ˈʌpˌbrɪŋ.ɪŋ/", "noun", "B1", "Sự nuôi dưỡng và giáo dục từ thời thơ ấu", "The treatment and instruction received by a child from its parents while growing up."),
        ("foster parent", "/ˈfɑː.stɚ ˌper.ənt/", "noun", "B2", "Cha mẹ nuôi dưỡng trẻ tạm thời", "An adult who cares for a child who is not their biological child."),
        ("affinity", "/əˈfɪn.ə.t̬i/", "noun", "B2", "Sự gần gũi thấu hiểu đồng điệu tâm hồn", "A spontaneous or natural liking or sympathy for someone or something."),
        ("fraternal", "/frəˈtɝː.nəl/", "adjective", "B2", "Thuộc về tình anh em ruột thịt", "Of or like a brother or brothers; brotherly."),
        ("maternal", "/məˈtɝː.nəl/", "adjective", "B1", "Thuộc về tình mẹ bao la", "Relating to a mother, especially during pregnancy or shortly after childbirth."),
        ("paternal", "/pəˈtɝː.nəl/", "adjective", "B1", "Thuộc về người cha trụ cột", "Appropriate to or characteristic of a father."),
        ("chaperon", "/ˈʃæp.ə.roʊn/", "verb", "B2", "Đi theo hộ tống giám sát thanh thiếu niên", "Accompany and look after someone as a chaperone."),
        ("alienation", "/ˌeɪ.li.əˈneɪ.ʃən/", "noun", "C1", "Cảm giác xa lánh cô lập với xã hội", "The state or experience of being isolated from a group or an activity to which one should belong."),
        ("solidarity", "/ˌsɑː.ləˈder.ə.t̬i/", "noun", "B2", "Tinh thần đoàn kết gắn bó keo sơn", "Mutual support within a group.")
    ],
    "Media, News & Communication": [
        ("broadcasting", "/ˈbrɑːdˌkæs.tɪŋ/", "noun", "B1", "Phát sóng chương trình trên đài hoặc truyền hình", "The transmission of programs or information by radio or television."),
        ("freelancer", "/ˈfriːˌlæn.sɚ/", "noun", "B1", "Phóng viên tự do không thuộc biên chế tòa soạn", "A person who works freelance, especially as an independent journalist."),
        ("columnist", "/ˈkɑː.ləm.nɪst/", "noun", "B2", "Cây bút chuyên mục bình luận riêng trên báo", "A journalist contributing regularly to a newspaper or magazine."),
        ("manuscript", "/ˈmæn.jə.skrɪpt/", "noun", "B2", "Bản thảo bài viết trước khi đưa in", "A book, document, or piece of music written by hand rather than typed or printed."),
        ("telecast", "/ˈtel.ə.kæst/", "noun", "B2", "Chương trình truyền hình phát sóng trực tiếp", "A television broadcast."),
        ("syndication", "/ˌsɪn.dəˈkeɪ.ʃən/", "noun", "C1", "Mua bán bản quyền phân phối nội dung tin tức cho nhiều báo", "The transfer of something for publication or broadcast simultaneously in a number of newspapers or television stations."),
        ("plagiarism", "/ˈpleɪ.dʒɚ.ɪ.zəm/", "noun", "B2", "Tội đạo văn sao chép ý tưởng bất hợp pháp", "The practice of taking someone else's work or ideas and passing them off as one's own."),
        ("libelous", "/ˈlaɪ.bəl.əs/", "adjective", "C1", "Mang tính phỉ báng xúc phạm danh dự qua văn bản", "Containing or constituting a libel; defamatory."),
        ("hyperbole", "/haɪˈpɝː.bəl.i/", "noun", "C1", "Cách nói cường điệu phóng đại quá mức", "Exaggerated statements or claims not meant to be taken literally."),
        ("newsroom", "/ˈnuːz.ruːm/", "noun", "B1", "Phòng biên tập tin tức sôi động của đài báo", "A room in a newspaper office or television station where news is received and prepared for publication."),
        ("airwaves", "/ˈer.weɪvz/", "noun", "B2", "Sóng phát thanh truyền hình phủ khắp nơi", "Radio and television as communication mediums."),
        ("disclaimer", "/dɪˈskleɪ.mɚ/", "noun", "B2", "Tuyên bố miễn trừ trách nhiệm về nội dung", "A statement that denies something, especially responsibility."),
        ("undercover", "/ˌʌn.dɚˈkʌv.ɚ/", "adjective", "B2", "Nhà báo đóng vai chìm điều tra mật", "Involved in or involving secret work within a community or organization, especially for investigation."),
        ("exclusive", "/ɪkˈskluː.sɪv/", "noun", "B1", "Bản tin độc quyền chỉ một tòa soạn có", "An item or story published or broadcast by only one newspaper or television station."),
        ("press conference", "/ˈpres ˌkɑːn.fɚ.əns/", "noun", "B1", "Buổi họp báo chính thức trả lời truyền thông", "An interview given to journalists by a prominent person in order to make an announcement or answer questions."),
        ("spokesperson", "/ˈspoʊksˌpɝː.sən/", "noun", "B2", "Người phát ngôn đại diện cho tổ chức", "A person who makes statements on behalf of a group or individual."),
        ("transcription", "/trænˈskrɪp.ʃən/", "noun", "B2", "Gỡ băng ghi âm thành văn bản viết", "A written or printed version of material originally presented in another medium."),
        ("newsletter", "/ˈnuːzˌlet̬.ɚ/", "noun", "A2", "Bản tin định kỳ gửi qua email cho độc giả", "A bulletin issued periodically to the members of a society, business, or organization."),
        ("byline", "/ˈbaɪ.laɪn/", "noun", "B2", "Dòng ghi tên tác giả bài báo dưới tiêu đề", "A line in a newspaper naming the writer of an article."),
        ("front page", "/ˌfrʌnt ˈpeɪdʒ/", "noun", "A2", "Trang nhất của tờ báo nơi đăng tin giật gân nhất", "The first page of a paper, containing the most important news."),
        ("breaking news", "/ˌbreɪ.kɪŋ ˈnuːz/", "noun", "A2", "Tin nóng hổi vừa mới xảy ra", "Newly received information about an event that is currently occurring or developing."),
        ("mass media", "/ˌmæs ˈmiː.di.ə/", "noun", "B1", "Phương tiện truyền thông đại chúng", "The media technologies intended to reach a large audience via mass communication.")
    ]
}

print(f"FILLER_TIER1 loaded: {len(FILLER_TIER1)} topics.")
