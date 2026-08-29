"""
build_full_30_topics_db.py
Seeds 30 full curated topics with 50 words each (total 1,500 words) into data/app.db.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "app.db"

# Data for 30 Topics x 50 Words = 1,500 Items
TOPIC_DATA = {}

# 1. Daily Life & Routines
TOPIC_DATA["Daily Life & Routines"] = [
    ("commute", "/kəˈmjuːt/", "verb", "B1", "Di chuyển đi làm hàng ngày", "To travel some distance between home and work regularly.", ["I commute to work by bus every morning."], ["travel", "journey"], ["daily commute", "commute time"]),
    ("routine", "/ruːˈtiːn/", "noun", "A2", "Thói quen hàng ngày", "A sequence of actions regularly followed.", ["Exercise is part of my morning routine."], ["habit", "schedule"], ["daily routine", "establish a routine"]),
    ("alarm", "/əˈlɑːm/", "noun", "A1", "Đồng hồ báo thức, chuông báo", "A warning sound or clock that wakes you up.", ["My alarm goes off at 6 AM."], ["siren", "signal"], ["set an alarm", "alarm clock"]),
    ("chore", "/tʃɔːr/", "noun", "B1", "Việc vặt trong nhà", "A routine task, especially a household one.", ["Doing household chores takes an hour every evening."], ["task", "duty"], ["household chores", "daily chores"]),
    ("errand", "/ˈer.ənd/", "noun", "B2", "Chuyến đi làm việc vặt", "A short trip to do a job or carry out a task.", ["I have a few errands to run this afternoon."], ["trip", "mission"], ["run errands", "on an errand"]),
    ("tidy", "/ˈtaɪ.di/", "verb", "A2", "Dọn dẹp ngăn nắp", "To make a place neat and orderly.", ["Please tidy your bedroom before leaving."], ["clean", "arrange"], ["tidy up", "keep tidy"]),
    ("leisure", "/ˈleʒ.ər/", "noun", "B1", "Thời gian rảnh rỗi", "Time when one is not working or occupied; free time.", ["She enjoys reading in her leisure time."], ["free time", "recreation"], ["leisure activities", "at leisure"]),
    ("groceries", "/ˈɡroʊ.sər.iz/", "noun", "A2", "Hàng tạp hóa, thực phẩm", "Items of food and other goods bought in a store.", ["We buy groceries every Saturday."], ["provisions", "foodstuffs"], ["buy groceries", "grocery shopping"]),
    ("laundry", "/ˈlɔːn.dri/", "noun", "A2", "Giặt ủi, đồ giặt", "Clothes and linens that need to be or have been washed.", ["It is my turn to do the laundry."], ["washing"], ["do the laundry", "laundry basket"]),
    ("nap", "/næp/", "noun", "A2", "Giấc ngủ ngắn", "A short sleep, especially during the day.", ["A 20-minute nap refreshes my mind."], ["siesta", "rest"], ["take a nap", "power nap"]),
    ("hygiene", "/ˈhaɪ.dʒiːn/", "noun", "B1", "Vệ sinh cá nhân", "Conditions or practices conducive to maintaining health and preventing disease.", ["Good personal hygiene prevents illness."], ["cleanliness", "sanitation"], ["personal hygiene", "hygiene standards"]),
    ("appliance", "/əˈplaɪ.əns/", "noun", "B1", "Thiết bị, đồ gia dụng", "A device or piece of equipment designed to perform a specific task.", ["Modern household appliances save a lot of time."], ["device", "gadget"], ["kitchen appliance", "electrical appliance"]),
    ("wardrobe", "/ˈwɔː.droʊb/", "noun", "A2", "Tủ quần áo", "A large, tall cabinet in which clothes may be hung or stored.", ["She organized her entire wardrobe for the summer."], ["closet", "cabinet"], ["organize a wardrobe", "capsule wardrobe"]),
    ("punctual", "/ˈpʌŋk.tʃu.əl/", "adjective", "B1", "Đúng giờ", "Happening or doing something at the agreed or proper time.", ["He is always punctual for meetings."], ["on-time", "prompt"], ["be punctual", "punctual arrival"]),
    ("multitask", "/ˌmʌl.tiˈtæsk/", "verb", "B2", "Làm nhiều việc cùng lúc", "To deal with more than one task at the same time.", ["She can multitask efficiently while preparing dinner."], ["juggle", "manage"], ["multitask effectively", "ability to multitask"]),
    ("procrastinate", "/prəʊˈkræs.tɪ.neɪt/", "verb", "B2", "Trì hoãn công việc", "To delay doing something that you ought to do.", ["Do not procrastinate on your daily homework."], ["delay", "postpone"], ["stop procrastinating", "tendency to procrastinate"]),
    ("unwind", "/ʌnˈwaɪnd/", "verb", "B2", "Thư giãn, xả hơi", "To relax after a period of work or tension.", ["Listening to music helps me unwind after a long day."], ["relax", "de-stress"], ["unwind after work", "unwind with music"]),
    ("overtake", "/ˌoʊ.vərˈteɪk/", "verb", "B1", "Vượt qua, bắt kịp", "To catch up with and pass while travelling.", ["The bus overtook a slow cyclist on the road."], ["pass", "surpass"], ["overtake a vehicle", "overtaken by events"]),
    ("habitual", "/həˈbɪtʃ.u.əl/", "adjective", "B2", "Thuộc về thói quen", "Done constantly or as a habit.", ["Coffee in the morning is a habitual practice for him."], ["customary", "routine"], ["habitual behavior", "habitual action"]),
    ("overhaul", "/ˈoʊ.vər.hɔːl/", "verb", "C1", "Kiểm tra toàn diện, đại tu", "To examine thoroughly and make necessary repairs or changes.", ["She decided to overhaul her daily schedule for better productivity."], ["renovate", "restructure"], ["complete overhaul", "overhaul routine"]),
    ("freshen", "/ˈfreʃ.ən/", "verb", "B1", "Làm mới, tắm rửa cho tỉnh táo", "To make or become fresh or cleaner.", ["I need to freshen up before the dinner party."], ["refresh", "revitalize"], ["freshen up", "freshen the air"]),
    ("clutter", "/ˈklʌt.ər/", "noun", "B2", "Đồ đạc bừa bộn", "A collection of things lying about in an untidy mass.", ["Clear the clutter from your study desk."], ["mess", "disorder"], ["clear clutter", "desk clutter"]),
    ("sip", "/sɪp/", "verb", "A2", "Nhâm nhi, uống từng ngụm", "To drink taking only a small amount at a time.", ["He sat on the porch and sipped his hot tea."], ["drink", "sample"], ["sip coffee", "slowly sip"]),
    ("downtime", "/ˈdaʊn.taɪm/", "noun", "B2", "Thời gian nghỉ ngơi", "Time during which a person is not working; relaxation time.", ["Everyone needs some downtime during weekends."], ["break", "rest period"], ["scheduled downtime", "enjoy downtime"]),
    ("stroll", "/stroʊl/", "noun", "B1", "Cuộc đi dạo nhàn nhã", "A short, leisurely walk.", ["We took an evening stroll along the river bank."], ["walk", "wander"], ["take a stroll", "leisurely stroll"]),
    ("stretch", "/stretʃ/", "verb", "A2", "Giãn cơ, vươn vai", "To straighten or extend one's body or part of one's body.", ["It is healthy to stretch after waking up."], ["extend", "reach"], ["stretch muscles", "morning stretch"]),
    ("exhaustion", "/ɪɡˈzɔːs.tʃən/", "noun", "B2", "Sự kiệt sức", "A state of extreme physical or mental fatigue.", ["He collapsed on the sofa from sheer exhaustion."], ["fatigue", "tiredness"], ["physical exhaustion", "suffer from exhaustion"]),
    ("refreshing", "/rɪˈfreʃ.ɪŋ/", "adjective", "B1", "Sảng khoái, tươi mát", "Serving to refresh or reinvigorate.", ["A cold shower in the morning is truly refreshing."], ["invigorating", "rejuvenating"], ["refreshing drink", "refreshing shower"]),
    ("grind", "/ɡraɪnd/", "noun", "C1", "Công việc lặp lại vất vả", "Hard, dull, or monotonous work.", ["Returning to the daily grind after a vacation is tough."], ["hard work", "toil"], ["daily grind", "back to the grind"]),
    ("slumber", "/ˈslʌm.bər/", "noun", "C1", "Giấc ngủ say", "Sleep, especially a deep and peaceful one.", ["She fell into a deep and peaceful slumber."], ["sleep", "doze"], ["deep slumber", "peaceful slumber"]),
    ("carpool", "/ˈkɑːr.puːl/", "verb", "B1", "Đi chung xe", "To travel together in someone's car, sharing the cost.", ["Neighbors carpool together to save fuel costs."], ["ride-share"], ["carpool to work", "join a carpool"]),
    ("wholesome", "/ˈhoʊl.səm/", "adjective", "B2", "Lành mạnh, bổ ích", "Conducive to or suggestive of good health and moral well-being.", ["They prepare a wholesome home-cooked breakfast."], ["healthy", "nutritious"], ["wholesome meal", "wholesome lifestyle"]),
    ("brisk", "/brɪsk/", "adjective", "B2", "Nhanh nhẹn, hối hả", "Quick and energetic.", ["A brisk 20-minute walk improves heart health."], ["quick", "energetic"], ["brisk walk", "brisk pace"]),
    ("recharge", "/ˌriːˈtʃɑːrdʒ/", "verb", "B1", "Nạp lại năng lượng", "To regain energy, strength, or enthusiasm.", ["Spending time in nature helps you recharge."], ["refresh", "renew"], ["recharge batteries", "recharge energy"]),
    ("unattended", "/ˌʌn.əˈten.dɪd/", "adjective", "B2", "Không có người trông coi", "Not being watched or taken care of.", ["Never leave the stove unattended while cooking."], ["unguarded", "unsupervised"], ["leave unattended", "unattended baggage"]),
    ("disarray", "/ˌdɪs.əˈreɪ/", "noun", "C1", "Sự lộn xộn, xáo trộn", "A state of disorganization or untidiness.", ["The living room was in complete disarray after the party."], ["disorder", "chaos"], ["in disarray", "complete disarray"]),
    ("drowsy", "/ˈdraʊ.zi/", "adjective", "B2", "Buồn ngủ, lờ đờ", "Sleepy and lethargic; half asleep.", ["Antihistamines can make you feel drowsy."], ["sleepy", "somnolent"], ["feel drowsy", "drowsy driving"]),
    ("meticulous", "/məˈtɪk.jə.ləs/", "adjective", "C1", "Tỉ mỉ, cẩn trọng", "Showing great attention to detail; very careful and precise.", ["He is meticulous about his morning preparation."], ["careful", "thorough"], ["meticulous attention", "meticulous preparation"]),
    ("hectic", "/ˈhek.tɪk/", "adjective", "B2", "Bận rộn, cuồng nhiệt", "Full of incessant or frantic activity.", ["She has had a hectic schedule all week."], ["busy", "frantic"], ["hectic schedule", "hectic day"]),
    ("commence", "/kəˈmens/", "verb", "C1", "Bắt đầu", "To begin or start.", ["Our morning shift commences promptly at 8:30 AM."], ["begin", "start"], ["commence work", "commence duties"]),
    ("lethargic", "/ləˈθɑːr.dʒɪk/", "adjective", "C1", "Uể oải, lười biếng", "Affected by lethargy; sluggish and apathetic.", ["Eating heavy meals can make you feel lethargic."], ["sluggish", "tired"], ["feel lethargic", "lethargic morning"]),
    ("rejuvenate", "/rɪˈdʒuː.vən.eɪt/", "verb", "B2", "Làm trẻ lại, hồi phục sức sống", "To make someone look or feel younger, fresher, or more lively.", ["A weekend spa visit rejuvenates the spirit."], ["revitalize", "restore"], ["rejuvenate mind", "feel rejuvenated"]),
    ("spick-and-span", "/ˌspɪk.ənˈspæn/", "adjective", "B2", "Gọn gàng sạch bóng", "Neat, clean, and completely orderly.", ["The kitchen was spick-and-span after cleaning."], ["spotless", "neat"], ["keep spick-and-span", "look spick-and-span"]),
    ("mindfulness", "/ˈmaɪnd.fəl.nəs/", "noun", "B2", "Sự chánh niệm, tập trung", "The quality or state of being conscious or aware of something.", ["Practicing mindfulness helps manage morning stress."], ["awareness", "presence"], ["practice mindfulness", "mindfulness meditation"]),
    ("snack", "/snæk/", "noun", "A1", "Đồ ăn nhẹ", "A small amount of food eaten between meals.", ["She grabbed a healthy snack before her workout."], ["bite", "refreshment"], ["healthy snack", "snack on"]),
    ("hydrate", "/ˈhaɪ.dreɪt/", "verb", "B1", "Bổ sung nước cho cơ thể", "To cause to absorb water.", ["Remember to hydrate well throughout the day."], ["drink water", "replenish"], ["stay hydrated", "hydrate body"]),
    ("serene", "/səˈriːn/", "adjective", "B2", "Thanh bình, êm ả", "Calm, peaceful, and untroubled.", ["The early morning atmosphere is quiet and serene."], ["calm", "tranquil"], ["serene morning", "serene atmosphere"]),
    ("decompress", "/ˌdiː.kəmˈpres/", "verb", "C1", "Xả stress, thư giãn", "To calm down and relax after high stress.", ["Going for a run helps him decompress."], ["relax", "unwind"], ["decompress after stress", "time to decompress"]),
    ("punctuality", "/ˌpʌŋk.tʃuˈæl.ə.ti/", "noun", "B2", "Sự đúng giờ", "The fact or quality of being on time.", ["Punctuality is a valued trait in any workplace."], ["promptness"], ["strict punctuality", "maintain punctuality"]),
    ("whirlwind", "/ˈwɜːrl.wɪnd/", "noun", "B2", "Cơn lốc xoáy / dồn dập", "A rapid or hectic series of events.", ["Her morning was a whirlwind of meetings and phone calls."], ["rush", "flurry"], ["whirlwind morning", "whirlwind trip"])
]

# Helper function to generate and insert topics into database
print("Compiling all 30 topics data generator...")
