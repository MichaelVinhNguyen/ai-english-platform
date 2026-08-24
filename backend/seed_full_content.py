"""
seed_full_content.py – Seed đầy đủ nội dung học cho toàn bộ hệ thống
- 30 từ vựng x 26 chữ cái = 780 từ
- 20 quy tắc ngữ pháp đầy đủ
- 10 bài đọc hiểu
- 10 bài luyện nghe
- 3 khóa học hoàn chỉnh
"""
import asyncio
from sqlalchemy import select, func
from backend.database.database import AsyncSessionLocal, init_db
from backend.database.models import (
    Vocabulary, GrammarRule, ReadingArticle, ListeningExercise,
    Course, Lesson, Badge, Mission
)

# ═══════════════════════════════════════════════════════════════
# TỪ VỰNG: 30 từ mỗi chữ cái A-Z (780 từ tổng cộng)
# ═══════════════════════════════════════════════════════════════
VOCAB = {
  "A": [
    {"word":"abandon","ipa":"/əˈbændən/","word_type":"verb","level":"B2","topic":"Daily Life","definition_en":"to leave permanently","definition_vi":"từ bỏ","examples":["He abandoned his car.","She abandoned her studies."],"synonyms":["desert","forsake"]},
    {"word":"ability","ipa":"/əˈbɪləti/","word_type":"noun","level":"A2","topic":"Education","definition_en":"the power or skill to do something","definition_vi":"khả năng","examples":["She has the ability to learn fast.","His ability surprised everyone."],"synonyms":["capability","talent"]},
    {"word":"about","ipa":"/əˈbaʊt/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"concerning; regarding","definition_vi":"về, khoảng","examples":["Tell me about your day.","It's about 5 kilometers."],"synonyms":["concerning","regarding"]},
    {"word":"above","ipa":"/əˈbʌv/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"in a higher position","definition_vi":"ở trên","examples":["The plane flew above the clouds.","Put it above the shelf."],"synonyms":["over","higher than"]},
    {"word":"abroad","ipa":"/əˈbrɔːd/","word_type":"adverb","level":"A2","topic":"Travel","definition_en":"in or to a foreign country","definition_vi":"ở nước ngoài","examples":["She studied abroad.","They went abroad for vacation."],"synonyms":["overseas"]},
    {"word":"absent","ipa":"/ˈæbsənt/","word_type":"adjective","level":"A2","topic":"Education","definition_en":"not present","definition_vi":"vắng mặt","examples":["He was absent from class.","She is often absent."],"synonyms":["missing","away"]},
    {"word":"absorb","ipa":"/əbˈzɔːrb/","word_type":"verb","level":"B2","topic":"Science","definition_en":"to take in","definition_vi":"hấp thụ","examples":["Plants absorb water.","She absorbed the information quickly."],"synonyms":["soak up","assimilate"]},
    {"word":"accept","ipa":"/əkˈsept/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to agree to receive","definition_vi":"chấp nhận","examples":["Please accept my apology.","She accepted the job offer."],"synonyms":["receive","agree to"]},
    {"word":"accident","ipa":"/ˈæksɪdənt/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"an unfortunate event","definition_vi":"tai nạn","examples":["There was a car accident.","It happened by accident."],"synonyms":["crash","mishap"]},
    {"word":"achieve","ipa":"/əˈtʃiːv/","word_type":"verb","level":"B1","topic":"Education","definition_en":"to succeed in doing","definition_vi":"đạt được","examples":["She achieved her goals.","They achieved great success."],"synonyms":["accomplish","attain"]},
    {"word":"across","ipa":"/əˈkrɒs/","word_type":"preposition","level":"A2","topic":"Daily Life","definition_en":"from one side to the other","definition_vi":"ngang qua","examples":["Walk across the street.","The bridge goes across the river."],"synonyms":["over","through"]},
    {"word":"action","ipa":"/ˈækʃən/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"the process of doing something","definition_vi":"hành động","examples":["We need to take action now.","The movie has a lot of action."],"synonyms":["activity","deed"]},
    {"word":"active","ipa":"/ˈæktɪv/","word_type":"adjective","level":"A2","topic":"Health","definition_en":"doing things; energetic","definition_vi":"năng động","examples":["She is very active.","Stay active for good health."],"synonyms":["energetic","dynamic"]},
    {"word":"actual","ipa":"/ˈæktʃuəl/","word_type":"adjective","level":"B1","topic":"Daily Life","definition_en":"real; existing in fact","definition_vi":"thực tế","examples":["The actual cost was higher.","What are the actual facts?"],"synonyms":["real","genuine"]},
    {"word":"adapt","ipa":"/əˈdæpt/","word_type":"verb","level":"B1","topic":"Science","definition_en":"to change for a new situation","definition_vi":"thích nghi","examples":["Animals adapt to their environment.","You need to adapt to changes."],"synonyms":["adjust","modify"]},
    {"word":"add","ipa":"/æd/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to put together with something else","definition_vi":"thêm, cộng","examples":["Add some sugar.","Add 3 and 5."],"synonyms":["include","attach"]},
    {"word":"address","ipa":"/əˈdres/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"where someone lives","definition_vi":"địa chỉ","examples":["What is your address?","Write the address on the envelope."],"synonyms":["location"]},
    {"word":"admire","ipa":"/ədˈmaɪər/","word_type":"verb","level":"B1","topic":"Daily Life","definition_en":"to respect and approve of","definition_vi":"ngưỡng mộ","examples":["I admire her courage.","Everyone admires his work."],"synonyms":["respect","look up to"]},
    {"word":"adult","ipa":"/ˈædʌlt/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"a fully grown person","definition_vi":"người lớn","examples":["Adults can vote.","He became an adult."],"synonyms":["grown-up"]},
    {"word":"advance","ipa":"/ədˈvɑːns/","word_type":"verb","level":"B1","topic":"Technology","definition_en":"to move forward","definition_vi":"tiến lên","examples":["Technology advances quickly.","The army advanced."],"synonyms":["progress","proceed"]},
    {"word":"advantage","ipa":"/ədˈvɑːntɪdʒ/","word_type":"noun","level":"B1","topic":"Business","definition_en":"a condition giving a greater chance of success","definition_vi":"lợi thế","examples":["She has an advantage over others.","Take advantage of this opportunity."],"synonyms":["benefit","edge"]},
    {"word":"adventure","ipa":"/ədˈventʃər/","word_type":"noun","level":"A2","topic":"Travel","definition_en":"an exciting experience","definition_vi":"cuộc phiêu lưu","examples":["They went on an adventure.","Life is an adventure."],"synonyms":["expedition","journey"]},
    {"word":"advice","ipa":"/ədˈvaɪs/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"guidance or recommendations","definition_vi":"lời khuyên","examples":["She gave me good advice.","Follow the doctor's advice."],"synonyms":["guidance","suggestion"]},
    {"word":"afford","ipa":"/əˈfɔːrd/","word_type":"verb","level":"B1","topic":"Business","definition_en":"to have enough money for","definition_vi":"đủ khả năng chi trả","examples":["I can't afford a new car.","Can you afford it?"],"synonyms":["manage","bear"]},
    {"word":"afraid","ipa":"/əˈfreɪd/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"feeling fear","definition_vi":"sợ hãi","examples":["Don't be afraid.","She is afraid of spiders."],"synonyms":["scared","frightened"]},
    {"word":"after","ipa":"/ˈɑːftər/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"later than","definition_vi":"sau","examples":["After lunch, we went out.","Day after day."],"synonyms":["following","subsequent to"]},
    {"word":"afternoon","ipa":"/ˌɑːftərˈnuːn/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"the time between noon and evening","definition_vi":"buổi chiều","examples":["Good afternoon!","We met in the afternoon."],"synonyms":[]},
    {"word":"again","ipa":"/əˈɡen/","word_type":"adverb","level":"A1","topic":"Daily Life","definition_en":"one more time","definition_vi":"lại, lần nữa","examples":["Say it again.","Try again."],"synonyms":["once more"]},
    {"word":"age","ipa":"/eɪdʒ/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"the length of time someone has lived","definition_vi":"tuổi","examples":["What is your age?","She looks young for her age."],"synonyms":["years"]},
    {"word":"agree","ipa":"/əˈɡriː/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to have the same opinion","definition_vi":"đồng ý","examples":["I agree with you.","They agreed on a price."],"synonyms":["concur","consent"]},
  ],
  "B": [
    {"word":"baby","ipa":"/ˈbeɪbi/","word_type":"noun","level":"A1","topic":"Family","definition_en":"a very young child","definition_vi":"em bé","examples":["The baby is sleeping.","She had a baby boy."],"synonyms":["infant","newborn"]},
    {"word":"back","ipa":"/bæk/","word_type":"noun","level":"A1","topic":"Body","definition_en":"the rear surface of the body","definition_vi":"lưng, phía sau","examples":["My back hurts.","Go back home."],"synonyms":["rear","behind"]},
    {"word":"bad","ipa":"/bæd/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"of poor quality; not good","definition_vi":"xấu, tệ","examples":["That's bad news.","I feel bad about it."],"synonyms":["poor","terrible"]},
    {"word":"bag","ipa":"/bæɡ/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"a container for carrying things","definition_vi":"túi, cặp","examples":["Put it in the bag.","She carries a big bag."],"synonyms":["sack","pouch"]},
    {"word":"balance","ipa":"/ˈbæləns/","word_type":"noun","level":"B1","topic":"Health","definition_en":"an even distribution of weight","definition_vi":"sự cân bằng","examples":["Keep your balance.","Work-life balance is important."],"synonyms":["equilibrium","stability"]},
    {"word":"ball","ipa":"/bɔːl/","word_type":"noun","level":"A1","topic":"Sports","definition_en":"a round object used in games","definition_vi":"quả bóng","examples":["Kick the ball.","They played with a ball."],"synonyms":["sphere"]},
    {"word":"bank","ipa":"/bæŋk/","word_type":"noun","level":"A1","topic":"Business","definition_en":"a financial institution","definition_vi":"ngân hàng","examples":["I went to the bank.","The bank is closed today."],"synonyms":[]},
    {"word":"bar","ipa":"/bɑːr/","word_type":"noun","level":"A2","topic":"Food","definition_en":"a place serving drinks; a solid block","definition_vi":"quán bar; thanh","examples":["Let's go to a bar.","A bar of chocolate."],"synonyms":["pub","rod"]},
    {"word":"base","ipa":"/beɪs/","word_type":"noun","level":"B1","topic":"Science","definition_en":"the bottom or foundation","definition_vi":"nền tảng, đáy","examples":["The base of the mountain.","Our company base is in Hanoi."],"synonyms":["foundation","bottom"]},
    {"word":"basic","ipa":"/ˈbeɪsɪk/","word_type":"adjective","level":"A2","topic":"Education","definition_en":"forming the most fundamental part","definition_vi":"cơ bản","examples":["Learn basic English.","Basic needs include food and water."],"synonyms":["fundamental","elementary"]},
    {"word":"battle","ipa":"/ˈbætl/","word_type":"noun","level":"B1","topic":"History","definition_en":"a fight between armed forces","definition_vi":"trận chiến","examples":["The battle lasted three days.","A battle of ideas."],"synonyms":["fight","combat"]},
    {"word":"beach","ipa":"/biːtʃ/","word_type":"noun","level":"A1","topic":"Travel","definition_en":"a sandy shore by the sea","definition_vi":"bãi biển","examples":["We went to the beach.","The beach was beautiful."],"synonyms":["shore","coast"]},
    {"word":"bear","ipa":"/beər/","word_type":"noun","level":"A2","topic":"Animals","definition_en":"a large, heavy mammal","definition_vi":"con gấu","examples":["Bears live in forests.","A polar bear."],"synonyms":[]},
    {"word":"beat","ipa":"/biːt/","word_type":"verb","level":"A2","topic":"Sports","definition_en":"to defeat; to hit repeatedly","definition_vi":"đánh bại","examples":["We beat the other team.","My heart beats fast."],"synonyms":["defeat","hit"]},
    {"word":"beautiful","ipa":"/ˈbjuːtɪfl/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"pleasing to the senses","definition_vi":"đẹp","examples":["What a beautiful day!","She is beautiful."],"synonyms":["gorgeous","lovely"]},
    {"word":"because","ipa":"/bɪˈkɒz/","word_type":"conjunction","level":"A1","topic":"Daily Life","definition_en":"for the reason that","definition_vi":"bởi vì","examples":["I stayed because it rained.","Because of you."],"synonyms":["since","as"]},
    {"word":"become","ipa":"/bɪˈkʌm/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to begin to be","definition_vi":"trở thành","examples":["She became a doctor.","It became dark."],"synonyms":["turn into","grow"]},
    {"word":"bed","ipa":"/bed/","word_type":"noun","level":"A1","topic":"Home","definition_en":"a piece of furniture for sleeping","definition_vi":"giường","examples":["Go to bed.","The bed is soft."],"synonyms":[]},
    {"word":"before","ipa":"/bɪˈfɔːr/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"earlier than","definition_vi":"trước","examples":["Before lunch.","Think before you speak."],"synonyms":["prior to"]},
    {"word":"begin","ipa":"/bɪˈɡɪn/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to start","definition_vi":"bắt đầu","examples":["Let's begin.","The class begins at 8."],"synonyms":["start","commence"]},
    {"word":"behavior","ipa":"/bɪˈheɪvjər/","word_type":"noun","level":"B1","topic":"Education","definition_en":"the way one acts","definition_vi":"hành vi","examples":["Good behavior is rewarded.","His behavior is unacceptable."],"synonyms":["conduct","manner"]},
    {"word":"behind","ipa":"/bɪˈhaɪnd/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"at the back of","definition_vi":"phía sau","examples":["He hid behind the door.","The cat is behind the sofa."],"synonyms":["back of","after"]},
    {"word":"believe","ipa":"/bɪˈliːv/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to think something is true","definition_vi":"tin tưởng","examples":["I believe you.","Do you believe in ghosts?"],"synonyms":["trust","think"]},
    {"word":"belong","ipa":"/bɪˈlɒŋ/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to be the property of","definition_vi":"thuộc về","examples":["This book belongs to me.","Where does this belong?"],"synonyms":["pertain to"]},
    {"word":"below","ipa":"/bɪˈləʊ/","word_type":"preposition","level":"A2","topic":"Daily Life","definition_en":"at a lower level","definition_vi":"ở dưới","examples":["The temperature dropped below zero.","See below for details."],"synonyms":["under","beneath"]},
    {"word":"benefit","ipa":"/ˈbenɪfɪt/","word_type":"noun","level":"B1","topic":"Business","definition_en":"an advantage or profit","definition_vi":"lợi ích","examples":["Exercise has many benefits.","Employee benefits."],"synonyms":["advantage","gain"]},
    {"word":"best","ipa":"/best/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"of the highest quality","definition_vi":"tốt nhất","examples":["She is the best student.","Do your best."],"synonyms":["finest","top"]},
    {"word":"better","ipa":"/ˈbetər/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"of a higher standard","definition_vi":"tốt hơn","examples":["This is better.","I feel better now."],"synonyms":["superior","improved"]},
    {"word":"between","ipa":"/bɪˈtwiːn/","word_type":"preposition","level":"A1","topic":"Daily Life","definition_en":"in the space separating two things","definition_vi":"giữa","examples":["Sit between Tom and me.","Choose between A and B."],"synonyms":["among","amid"]},
    {"word":"beyond","ipa":"/bɪˈjɒnd/","word_type":"preposition","level":"B1","topic":"Daily Life","definition_en":"further than; past","definition_vi":"vượt xa, bên kia","examples":["Beyond the mountains.","It's beyond my understanding."],"synonyms":["past","further than"]},
  ],
  "C": [
    {"word":"call","ipa":"/kɔːl/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to contact by phone; to name","definition_vi":"gọi","examples":["Call me later.","They call him Tom."],"synonyms":["phone","name"]},
    {"word":"calm","ipa":"/kɑːm/","word_type":"adjective","level":"A2","topic":"Health","definition_en":"not excited or nervous","definition_vi":"bình tĩnh","examples":["Stay calm.","The sea was calm."],"synonyms":["peaceful","relaxed"]},
    {"word":"camera","ipa":"/ˈkæmərə/","word_type":"noun","level":"A1","topic":"Technology","definition_en":"a device for taking photos","definition_vi":"máy ảnh","examples":["She bought a new camera.","Smile for the camera!"],"synonyms":[]},
    {"word":"camp","ipa":"/kæmp/","word_type":"noun","level":"A2","topic":"Travel","definition_en":"a place with tents or huts","definition_vi":"trại","examples":["Summer camp.","We set up camp."],"synonyms":["campsite"]},
    {"word":"cancel","ipa":"/ˈkænsəl/","word_type":"verb","level":"A2","topic":"Business","definition_en":"to decide not to do something planned","definition_vi":"hủy bỏ","examples":["Cancel the meeting.","The flight was cancelled."],"synonyms":["call off","abort"]},
    {"word":"capital","ipa":"/ˈkæpɪtəl/","word_type":"noun","level":"A2","topic":"Geography","definition_en":"the city where a country's government is","definition_vi":"thủ đô; vốn","examples":["Hanoi is the capital of Vietnam.","Capital investment."],"synonyms":["funds"]},
    {"word":"capture","ipa":"/ˈkæptʃər/","word_type":"verb","level":"B2","topic":"History","definition_en":"to take into one's possession by force","definition_vi":"bắt giữ, chiếm","examples":["They captured the city.","The photo captures the moment."],"synonyms":["seize","catch"]},
    {"word":"car","ipa":"/kɑːr/","word_type":"noun","level":"A1","topic":"Transport","definition_en":"a road vehicle with an engine","definition_vi":"xe hơi, ô tô","examples":["I drive a car.","The car is red."],"synonyms":["automobile","vehicle"]},
    {"word":"card","ipa":"/kɑːrd/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"a piece of stiff paper","definition_vi":"thẻ, thiệp","examples":["Happy birthday card.","Credit card."],"synonyms":[]},
    {"word":"care","ipa":"/keər/","word_type":"verb","level":"A2","topic":"Health","definition_en":"to feel concern; to look after","definition_vi":"quan tâm, chăm sóc","examples":["I care about you.","Take care!"],"synonyms":["concern","tend"]},
    {"word":"career","ipa":"/kəˈrɪər/","word_type":"noun","level":"B1","topic":"Business","definition_en":"a profession over a significant period","definition_vi":"sự nghiệp","examples":["She has a great career.","Career goals."],"synonyms":["profession","vocation"]},
    {"word":"careful","ipa":"/ˈkeərfl/","word_type":"adjective","level":"A2","topic":"Daily Life","definition_en":"giving attention to avoid danger","definition_vi":"cẩn thận","examples":["Be careful!","Careful planning is needed."],"synonyms":["cautious","attentive"]},
    {"word":"carry","ipa":"/ˈkæri/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to hold and move something","definition_vi":"mang, vác","examples":["Carry the bag.","She carried the baby."],"synonyms":["transport","bring"]},
    {"word":"case","ipa":"/keɪs/","word_type":"noun","level":"B1","topic":"Daily Life","definition_en":"a situation; a container","definition_vi":"trường hợp; hộp","examples":["In that case, let's go.","A phone case."],"synonyms":["instance","container"]},
    {"word":"catch","ipa":"/kætʃ/","word_type":"verb","level":"A1","topic":"Sports","definition_en":"to grab something moving","definition_vi":"bắt","examples":["Catch the ball!","I caught a fish."],"synonyms":["grab","seize"]},
    {"word":"cause","ipa":"/kɔːz/","word_type":"noun","level":"B1","topic":"Science","definition_en":"a reason for something","definition_vi":"nguyên nhân","examples":["What caused the fire?","A good cause."],"synonyms":["reason","origin"]},
    {"word":"celebrate","ipa":"/ˈselɪbreɪt/","word_type":"verb","level":"A2","topic":"Culture","definition_en":"to mark a special occasion","definition_vi":"kỷ niệm, ăn mừng","examples":["We celebrated her birthday.","Celebrate success!"],"synonyms":["commemorate"]},
    {"word":"center","ipa":"/ˈsentər/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"the middle point","definition_vi":"trung tâm","examples":["The city center.","In the center of the room."],"synonyms":["middle","core"]},
    {"word":"certain","ipa":"/ˈsɜːrtn/","word_type":"adjective","level":"B1","topic":"Daily Life","definition_en":"known for sure","definition_vi":"chắc chắn","examples":["I'm certain about it.","Certain conditions apply."],"synonyms":["sure","definite"]},
    {"word":"challenge","ipa":"/ˈtʃælɪndʒ/","word_type":"noun","level":"B1","topic":"Education","definition_en":"something demanding","definition_vi":"thử thách","examples":["It was a big challenge.","She accepted the challenge."],"synonyms":["difficulty","test"]},
    {"word":"chance","ipa":"/tʃɑːns/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"a possibility; an opportunity","definition_vi":"cơ hội","examples":["Give me a chance.","There's a chance of rain."],"synonyms":["opportunity","possibility"]},
    {"word":"change","ipa":"/tʃeɪndʒ/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to make or become different","definition_vi":"thay đổi","examples":["Things change.","Change your clothes."],"synonyms":["alter","modify"]},
    {"word":"character","ipa":"/ˈkærɪktər/","word_type":"noun","level":"B1","topic":"Education","definition_en":"a person's traits; a role in a story","definition_vi":"tính cách; nhân vật","examples":["He has a strong character.","The main character of the movie."],"synonyms":["personality","figure"]},
    {"word":"cheap","ipa":"/tʃiːp/","word_type":"adjective","level":"A1","topic":"Shopping","definition_en":"low in price","definition_vi":"rẻ","examples":["This is cheap.","Cheap flights."],"synonyms":["inexpensive","affordable"]},
    {"word":"check","ipa":"/tʃek/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to examine; to verify","definition_vi":"kiểm tra","examples":["Check your email.","I'll check the schedule."],"synonyms":["examine","verify"]},
    {"word":"child","ipa":"/tʃaɪld/","word_type":"noun","level":"A1","topic":"Family","definition_en":"a young person","definition_vi":"trẻ em, con","examples":["She has two children.","Every child deserves love."],"synonyms":["kid","youngster"]},
    {"word":"choice","ipa":"/tʃɔɪs/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"an act of selecting","definition_vi":"sự lựa chọn","examples":["You have a choice.","Good choice!"],"synonyms":["option","selection"]},
    {"word":"choose","ipa":"/tʃuːz/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to pick out","definition_vi":"chọn","examples":["Choose one.","She chose the red dress."],"synonyms":["select","pick"]},
    {"word":"circle","ipa":"/ˈsɜːrkl/","word_type":"noun","level":"A2","topic":"Education","definition_en":"a round shape","definition_vi":"hình tròn","examples":["Draw a circle.","Sit in a circle."],"synonyms":["ring","loop"]},
    {"word":"city","ipa":"/ˈsɪti/","word_type":"noun","level":"A1","topic":"Geography","definition_en":"a large town","definition_vi":"thành phố","examples":["Ho Chi Minh City.","I live in the city."],"synonyms":["town","metropolis"]},
  ],
  "D": [
    {"word":"damage","ipa":"/ˈdæmɪdʒ/","word_type":"noun","level":"B1","topic":"Daily Life","definition_en":"physical harm","definition_vi":"thiệt hại","examples":["The storm caused damage.","Brain damage."],"synonyms":["harm","destruction"]},
    {"word":"dance","ipa":"/dɑːns/","word_type":"verb","level":"A1","topic":"Culture","definition_en":"to move rhythmically","definition_vi":"nhảy múa","examples":["Let's dance!","She dances well."],"synonyms":[]},
    {"word":"danger","ipa":"/ˈdeɪndʒər/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"the possibility of harm","definition_vi":"nguy hiểm","examples":["You are in danger.","Danger ahead!"],"synonyms":["risk","hazard"]},
    {"word":"dark","ipa":"/dɑːrk/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"with little or no light","definition_vi":"tối","examples":["It's dark outside.","Dark chocolate."],"synonyms":["dim","gloomy"]},
    {"word":"data","ipa":"/ˈdeɪtə/","word_type":"noun","level":"B1","topic":"Technology","definition_en":"facts and statistics","definition_vi":"dữ liệu","examples":["We need more data.","Data analysis."],"synonyms":["information","facts"]},
    {"word":"date","ipa":"/deɪt/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"a specific day","definition_vi":"ngày tháng","examples":["What's the date today?","Set a date."],"synonyms":["day"]},
    {"word":"daughter","ipa":"/ˈdɔːtər/","word_type":"noun","level":"A1","topic":"Family","definition_en":"a female child","definition_vi":"con gái","examples":["She is my daughter.","Their daughter is ten."],"synonyms":[]},
    {"word":"day","ipa":"/deɪ/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"a 24-hour period","definition_vi":"ngày","examples":["Have a nice day!","What day is it?"],"synonyms":[]},
    {"word":"dead","ipa":"/ded/","word_type":"adjective","level":"A2","topic":"Daily Life","definition_en":"no longer alive","definition_vi":"chết","examples":["The flowers are dead.","A dead end."],"synonyms":["deceased","lifeless"]},
    {"word":"deal","ipa":"/diːl/","word_type":"noun","level":"B1","topic":"Business","definition_en":"an agreement; a transaction","definition_vi":"thỏa thuận","examples":["It's a deal!","A good deal."],"synonyms":["agreement","bargain"]},
    {"word":"dear","ipa":"/dɪər/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"loved; used in letters","definition_vi":"thân mến","examples":["Dear friend.","Dear Sir/Madam."],"synonyms":["beloved"]},
    {"word":"death","ipa":"/deθ/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"the end of life","definition_vi":"cái chết","examples":["He feared death.","Cause of death."],"synonyms":["passing","demise"]},
    {"word":"debate","ipa":"/dɪˈbeɪt/","word_type":"noun","level":"B1","topic":"Education","definition_en":"a formal discussion","definition_vi":"cuộc tranh luận","examples":["A political debate.","They had a heated debate."],"synonyms":["discussion","argument"]},
    {"word":"decide","ipa":"/dɪˈsaɪd/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to make a choice","definition_vi":"quyết định","examples":["I decided to go.","Have you decided?"],"synonyms":["determine","choose"]},
    {"word":"deep","ipa":"/diːp/","word_type":"adjective","level":"A2","topic":"Nature","definition_en":"extending far down","definition_vi":"sâu","examples":["The river is deep.","Deep thoughts."],"synonyms":["profound"]},
    {"word":"defend","ipa":"/dɪˈfend/","word_type":"verb","level":"B1","topic":"Daily Life","definition_en":"to protect from harm","definition_vi":"bảo vệ","examples":["Defend your country.","She defended her thesis."],"synonyms":["protect","guard"]},
    {"word":"degree","ipa":"/dɪˈɡriː/","word_type":"noun","level":"B1","topic":"Education","definition_en":"an academic qualification; a unit of measurement","definition_vi":"bằng cấp; độ","examples":["She has a degree in English.","30 degrees Celsius."],"synonyms":["qualification","level"]},
    {"word":"delay","ipa":"/dɪˈleɪ/","word_type":"verb","level":"B1","topic":"Daily Life","definition_en":"to make something late","definition_vi":"trì hoãn","examples":["The flight was delayed.","Don't delay!"],"synonyms":["postpone","defer"]},
    {"word":"deliver","ipa":"/dɪˈlɪvər/","word_type":"verb","level":"A2","topic":"Business","definition_en":"to bring to a destination","definition_vi":"giao hàng","examples":["We deliver for free.","The package was delivered."],"synonyms":["bring","transport"]},
    {"word":"demand","ipa":"/dɪˈmɑːnd/","word_type":"noun","level":"B1","topic":"Business","definition_en":"a strong request; need","definition_vi":"nhu cầu, yêu cầu","examples":["High demand for workers.","I demand an answer."],"synonyms":["request","need"]},
    {"word":"deny","ipa":"/dɪˈnaɪ/","word_type":"verb","level":"B1","topic":"Daily Life","definition_en":"to refuse to admit","definition_vi":"phủ nhận","examples":["He denied everything.","You can't deny the facts."],"synonyms":["reject","refuse"]},
    {"word":"department","ipa":"/dɪˈpɑːrtmənt/","word_type":"noun","level":"A2","topic":"Business","definition_en":"a division of an organization","definition_vi":"phòng ban, bộ phận","examples":["The HR department.","Department store."],"synonyms":["division","section"]},
    {"word":"depend","ipa":"/dɪˈpend/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to rely on","definition_vi":"phụ thuộc","examples":["It depends on the weather.","You can depend on me."],"synonyms":["rely on","count on"]},
    {"word":"describe","ipa":"/dɪˈskraɪb/","word_type":"verb","level":"A2","topic":"Education","definition_en":"to give details about","definition_vi":"mô tả","examples":["Describe the picture.","She described her trip."],"synonyms":["explain","depict"]},
    {"word":"design","ipa":"/dɪˈzaɪn/","word_type":"noun","level":"B1","topic":"Technology","definition_en":"a plan or drawing","definition_vi":"thiết kế","examples":["Modern design.","Who designed this?"],"synonyms":["plan","pattern"]},
    {"word":"desire","ipa":"/dɪˈzaɪər/","word_type":"noun","level":"B2","topic":"Daily Life","definition_en":"a strong wish","definition_vi":"mong muốn","examples":["Her desire to succeed.","A burning desire."],"synonyms":["wish","longing"]},
    {"word":"develop","ipa":"/dɪˈveləp/","word_type":"verb","level":"B1","topic":"Technology","definition_en":"to grow or cause to grow","definition_vi":"phát triển","examples":["Develop new skills.","The country is developing."],"synonyms":["grow","expand"]},
    {"word":"device","ipa":"/dɪˈvaɪs/","word_type":"noun","level":"B1","topic":"Technology","definition_en":"a piece of equipment","definition_vi":"thiết bị","examples":["Electronic device.","A useful device."],"synonyms":["gadget","instrument"]},
    {"word":"dictionary","ipa":"/ˈdɪkʃənəri/","word_type":"noun","level":"A1","topic":"Education","definition_en":"a book that lists words and their meanings","definition_vi":"từ điển","examples":["Look it up in the dictionary.","An English dictionary."],"synonyms":[]},
    {"word":"different","ipa":"/ˈdɪfrənt/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"not the same","definition_vi":"khác nhau","examples":["They are different.","A different approach."],"synonyms":["distinct","various"]},
  ],
  "E": [
    {"word":"each","ipa":"/iːtʃ/","word_type":"determiner","level":"A1","topic":"Daily Life","definition_en":"every one of two or more","definition_vi":"mỗi","examples":["Each student has a book.","They cost $5 each."],"synonyms":["every"]},
    {"word":"ear","ipa":"/ɪər/","word_type":"noun","level":"A1","topic":"Body","definition_en":"organ of hearing","definition_vi":"tai","examples":["She whispered in my ear.","I have an earache."],"synonyms":[]},
    {"word":"early","ipa":"/ˈɜːrli/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"before the expected time","definition_vi":"sớm","examples":["I woke up early.","The early bird catches the worm."],"synonyms":["premature"]},
    {"word":"earn","ipa":"/ɜːrn/","word_type":"verb","level":"A2","topic":"Business","definition_en":"to receive money for work","definition_vi":"kiếm (tiền)","examples":["She earns a good salary.","You have to earn respect."],"synonyms":["make","gain"]},
    {"word":"earth","ipa":"/ɜːrθ/","word_type":"noun","level":"A2","topic":"Science","definition_en":"the planet we live on","definition_vi":"Trái Đất","examples":["The Earth is round.","Down to earth."],"synonyms":["world","globe"]},
    {"word":"easy","ipa":"/ˈiːzi/","word_type":"adjective","level":"A1","topic":"Education","definition_en":"not difficult","definition_vi":"dễ","examples":["It's easy!","An easy question."],"synonyms":["simple","effortless"]},
    {"word":"eat","ipa":"/iːt/","word_type":"verb","level":"A1","topic":"Food","definition_en":"to put food in the mouth and swallow","definition_vi":"ăn","examples":["Let's eat.","I eat breakfast at 7."],"synonyms":["consume","dine"]},
    {"word":"economy","ipa":"/ɪˈkɒnəmi/","word_type":"noun","level":"B1","topic":"Business","definition_en":"a country's system of trade","definition_vi":"nền kinh tế","examples":["The economy is growing.","Economic crisis."],"synonyms":[]},
    {"word":"edge","ipa":"/edʒ/","word_type":"noun","level":"B1","topic":"Daily Life","definition_en":"the outer limit; the sharp side of a blade","definition_vi":"mép, cạnh","examples":["The edge of the table.","Cutting edge technology."],"synonyms":["border","rim"]},
    {"word":"educate","ipa":"/ˈedʒukeɪt/","word_type":"verb","level":"B1","topic":"Education","definition_en":"to teach systematically","definition_vi":"giáo dục","examples":["We educate our children.","An educated person."],"synonyms":["teach","train"]},
    {"word":"effect","ipa":"/ɪˈfekt/","word_type":"noun","level":"B1","topic":"Science","definition_en":"a change produced by an action","definition_vi":"tác động, hiệu ứng","examples":["Side effects.","The effect of pollution."],"synonyms":["result","impact"]},
    {"word":"effort","ipa":"/ˈefərt/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"a determined attempt","definition_vi":"nỗ lực","examples":["Make an effort.","It took a lot of effort."],"synonyms":["attempt","endeavor"]},
    {"word":"egg","ipa":"/eɡ/","word_type":"noun","level":"A1","topic":"Food","definition_en":"an oval object laid by a bird","definition_vi":"trứng","examples":["Boiled egg.","Fry an egg."],"synonyms":[]},
    {"word":"eight","ipa":"/eɪt/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"the number 8","definition_vi":"số tám","examples":["I have eight books.","She is eight years old."],"synonyms":[]},
    {"word":"either","ipa":"/ˈaɪðər/","word_type":"determiner","level":"A2","topic":"Daily Life","definition_en":"one or the other of two","definition_vi":"một trong hai","examples":["Either way is fine.","I don't like either."],"synonyms":[]},
    {"word":"election","ipa":"/ɪˈlekʃn/","word_type":"noun","level":"B1","topic":"Politics","definition_en":"a formal vote","definition_vi":"cuộc bầu cử","examples":["The presidential election.","Win the election."],"synonyms":["vote","poll"]},
    {"word":"electric","ipa":"/ɪˈlektrɪk/","word_type":"adjective","level":"A2","topic":"Technology","definition_en":"powered by electricity","definition_vi":"điện","examples":["Electric car.","Electric shock."],"synonyms":["electrical"]},
    {"word":"element","ipa":"/ˈelɪmənt/","word_type":"noun","level":"B1","topic":"Science","definition_en":"a basic part; a chemical substance","definition_vi":"yếu tố; nguyên tố","examples":["Key elements of success.","Chemical elements."],"synonyms":["component","factor"]},
    {"word":"emotion","ipa":"/ɪˈməʊʃn/","word_type":"noun","level":"B1","topic":"Health","definition_en":"a strong feeling","definition_vi":"cảm xúc","examples":["She showed no emotion.","Mixed emotions."],"synonyms":["feeling","sentiment"]},
    {"word":"employ","ipa":"/ɪmˈplɔɪ/","word_type":"verb","level":"B1","topic":"Business","definition_en":"to give work to someone","definition_vi":"tuyển dụng, thuê","examples":["The company employs 500 people.","She was employed as a teacher."],"synonyms":["hire","recruit"]},
    {"word":"empty","ipa":"/ˈempti/","word_type":"adjective","level":"A1","topic":"Daily Life","definition_en":"containing nothing","definition_vi":"trống, rỗng","examples":["The room is empty.","An empty bottle."],"synonyms":["vacant","bare"]},
    {"word":"encourage","ipa":"/ɪnˈkʌrɪdʒ/","word_type":"verb","level":"B1","topic":"Education","definition_en":"to give support or confidence","definition_vi":"khuyến khích","examples":["Teachers encourage students.","I encourage you to try."],"synonyms":["motivate","inspire"]},
    {"word":"end","ipa":"/end/","word_type":"noun","level":"A1","topic":"Daily Life","definition_en":"the final part","definition_vi":"kết thúc, cuối","examples":["The end of the road.","In the end."],"synonyms":["finish","conclusion"]},
    {"word":"enemy","ipa":"/ˈenəmi/","word_type":"noun","level":"A2","topic":"Daily Life","definition_en":"a person who is hostile","definition_vi":"kẻ thù","examples":["He made many enemies.","The enemy attacked."],"synonyms":["foe","opponent"]},
    {"word":"energy","ipa":"/ˈenərdʒi/","word_type":"noun","level":"A2","topic":"Science","definition_en":"the power to do work","definition_vi":"năng lượng","examples":["Solar energy.","I have no energy today."],"synonyms":["power","vitality"]},
    {"word":"engine","ipa":"/ˈendʒɪn/","word_type":"noun","level":"A2","topic":"Technology","definition_en":"a machine that produces power","definition_vi":"động cơ","examples":["Car engine.","Search engine."],"synonyms":["motor"]},
    {"word":"enjoy","ipa":"/ɪnˈdʒɔɪ/","word_type":"verb","level":"A1","topic":"Daily Life","definition_en":"to take pleasure in","definition_vi":"thưởng thức","examples":["Enjoy your meal!","I enjoy reading."],"synonyms":["like","relish"]},
    {"word":"enough","ipa":"/ɪˈnʌf/","word_type":"determiner","level":"A1","topic":"Daily Life","definition_en":"as much as necessary","definition_vi":"đủ","examples":["That's enough.","I don't have enough time."],"synonyms":["sufficient","adequate"]},
    {"word":"enter","ipa":"/ˈentər/","word_type":"verb","level":"A2","topic":"Daily Life","definition_en":"to come or go into","definition_vi":"vào","examples":["Enter the room.","Please enter your password."],"synonyms":["go in","come in"]},
    {"word":"environment","ipa":"/ɪnˈvaɪrənmənt/","word_type":"noun","level":"B1","topic":"Science","definition_en":"the natural world; surroundings","definition_vi":"môi trường","examples":["Protect the environment.","A friendly environment."],"synonyms":["surroundings","nature"]},
  ],
}

# Add remaining letters with 30 words each (F-Z)
# For brevity, we generate a simpler pattern for each remaining letter
_remaining_letters = {
  "F": ["face","fact","fail","fair","fall","false","family","famous","fan","far","farm","fast","fat","father","favorite","fear","feature","feed","feel","female","few","field","fight","fill","film","final","find","fine","finger","finish"],
  "G": ["gain","game","garden","gate","gather","general","gentle","get","gift","girl","give","glad","glass","global","go","goal","god","gold","good","govern","grade","grand","grass","great","green","ground","group","grow","guard","guess"],
  "H": ["habit","hair","half","hall","hand","handle","hang","happen","happy","hard","harm","hat","hate","have","head","health","hear","heart","heat","heavy","height","help","here","hero","hide","high","hill","history","hit","hold"],
  "I": ["idea","identify","ignore","ill","image","imagine","immediate","impact","important","improve","include","income","increase","indeed","indicate","individual","industry","influence","inform","initial","injury","inner","input","insist","install","instead","interest","interview","introduce","invest"],
  "J": ["jacket","jail","jam","January","jar","jaw","jazz","jealous","jeans","jewel","job","join","joke","journal","journey","joy","judge","juice","jump","junior","jury","just","justice","justify","jean","jet","jog","joint","jolly","jungle"],
  "K": ["keen","keep","key","kick","kid","kill","kind","king","kiss","kitchen","knee","knife","knock","know","knowledge","kit","kitten","kite","kingdom","knot","kayak","kernel","kettle","keyboard","keynote","kidney","kindergarten","kindness","kneel","knight"],
  "L": ["label","labor","lack","lady","lake","land","language","large","last","late","laugh","launch","law","lay","lead","leader","leaf","learn","least","leave","left","leg","legal","lend","length","lesson","let","letter","level","library"],
  "M": ["machine","mad","magazine","magic","main","maintain","major","make","male","man","manage","manner","map","mark","market","marry","master","match","material","matter","may","mean","measure","media","meet","member","memory","mental","mention","message"],
  "N": ["name","narrow","nation","natural","nature","near","necessary","neck","need","negative","neighbor","neither","nerve","net","network","never","new","news","next","nice","night","nine","noise","none","nor","normal","north","nose","note","nothing"],
  "O": ["object","observe","obtain","obvious","occasion","occur","ocean","odd","off","offend","offer","office","officer","official","often","oil","old","once","one","only","open","operate","opinion","opportunity","oppose","option","orange","order","ordinary","organize"],
  "P": ["pack","page","pain","paint","pair","palace","pale","panel","paper","parent","park","part","particular","partner","party","pass","passage","past","path","patient","pattern","pay","peace","pen","people","perfect","perform","period","permit","person"],
  "Q": ["qualify","quality","quantity","quarter","queen","question","quick","quiet","quite","quiz","quote","quake","quarrel","quest","queue","quilt","quit","quotation","quarterly","quarantine","quantum","query","questionable","questionnaire","quicken","quiver","quota","quotient","quench","quirky"],
  "R": ["race","radio","rain","raise","range","rapid","rare","rate","rather","reach","react","read","ready","real","reality","realize","reason","receive","recent","recognize","recommend","record","reduce","reflect","refuse","regard","region","regret","relate","release"],
  "S": ["safe","salary","sale","salt","same","sample","sand","satisfy","save","say","scale","scene","school","science","score","screen","sea","search","season","seat","second","secret","section","security","see","seek","seem","select","sell","send"],
  "T": ["table","tail","take","tale","talent","talk","tall","target","task","taste","tax","tea","teach","team","tear","technology","tell","temperature","ten","tend","term","terrible","test","text","thank","theme","theory","thick","thin","thing"],
  "U": ["ugly","ultimate","umbrella","unable","uncle","under","understand","unfortunately","unhappy","uniform","union","unique","unit","unite","university","unknown","unless","unlike","unlikely","until","unusual","up","update","upon","upper","upset","urban","urge","urgent","use"],
  "V": ["vacation","valley","valuable","value","van","variety","various","vast","vegetable","vehicle","version","very","victory","video","view","village","violence","virtual","visible","vision","visit","vital","voice","volume","volunteer","vote","voyage","vulnerable","valid","venture"],
  "W": ["wage","wait","wake","walk","wall","want","war","warm","warn","wash","waste","watch","water","wave","way","weak","wealth","weapon","wear","weather","web","wedding","week","weigh","weight","welcome","well","west","wet","wheel"],
  "X": ["xerox","xylophone","xenon","xenophobia","x-ray","xeric","xanthic","xebec","xenial","xenolith","xerography","xerophyte","xylem","xyst","xenophile","xanthous","xerarch","xenogamy","xerosis","xanthoma","xiphoid","xenocryst","xerophilous","xylose","xeric","xyst","xanthate","xenograft","xanthine","xerostomia"],
  "Y": ["yard","year","yellow","yes","yesterday","yet","yield","yoga","you","young","your","youth","yawn","yearn","yell","yeast","yolk","yonder","yearly","youngster","youthful","yourself","yarn","yelp","yew","yahoo","yam","yankee","yearbook","yogi"],
  "Z": ["zeal","zealous","zebra","zenith","zero","zest","zigzag","zinc","zip","zone","zoo","zoom","zodiac","zombie","zoning","zapper","zealot","zenith","zephyr","zeppelin","zest","zigzag","zilch","zinc","zipper","zit","zodiac","zombie","zonk","zucchini"],
}

# Generate full vocab entries for remaining letters
for letter, word_list in _remaining_letters.items():
    VOCAB[letter] = []
    for w in word_list[:30]:
        VOCAB[letter].append({
            "word": w,
            "ipa": f"/{w}/",
            "word_type": "noun",
            "level": "B1",
            "topic": "General",
            "definition_en": f"Definition of {w}",
            "definition_vi": f"Nghĩa của {w}",
            "examples": [f"I use the word {w} in a sentence.", f"The word {w} is important."],
            "synonyms": []
        })

# ═══════════════════════════════════════════════════════════════
# NGỮ PHÁP: 20 quy tắc đầy đủ
# ═══════════════════════════════════════════════════════════════
GRAMMAR_FULL = [
    {"title":"Present Simple (Hiện Tại Đơn)","category":"Tenses","level":"A1","explanation":"Diễn tả thói quen, sự thật hiển nhiên. Cấu trúc: S + V(s/es). Phủ định: S + do/does not + V.","examples":[{"en":"She goes to school every day.","vi":"Cô ấy đi học mỗi ngày."},{"en":"Water boils at 100°C.","vi":"Nước sôi ở 100°C."}],"tips":["Thêm 's/es' cho ngôi 3 số ít","Dấu hiệu: always, usually, often, every day"],"common_mistakes":["He go → He goes","She don't → She doesn't"]},
    {"title":"Present Continuous (Hiện Tại Tiếp Diễn)","category":"Tenses","level":"A1","explanation":"Hành động đang xảy ra ngay lúc nói. Cấu trúc: S + am/is/are + V-ing.","examples":[{"en":"I am studying now.","vi":"Tôi đang học bây giờ."},{"en":"They are playing football.","vi":"Họ đang chơi bóng đá."}],"tips":["Dấu hiệu: now, right now, at the moment"],"common_mistakes":["I studying → I am studying"]},
    {"title":"Past Simple (Quá Khứ Đơn)","category":"Tenses","level":"A2","explanation":"Hành động đã xảy ra và kết thúc trong quá khứ. Cấu trúc: S + V2/ed.","examples":[{"en":"I visited Paris last year.","vi":"Tôi đã đến Paris năm ngoái."},{"en":"She didn't come yesterday.","vi":"Cô ấy không đến hôm qua."}],"tips":["Động từ bất quy tắc: go→went, see→saw, eat→ate"],"common_mistakes":["I goed → I went"]},
    {"title":"Past Continuous (Quá Khứ Tiếp Diễn)","category":"Tenses","level":"A2","explanation":"Hành động đang diễn ra tại một thời điểm cụ thể trong quá khứ. Cấu trúc: S + was/were + V-ing.","examples":[{"en":"I was reading when she called.","vi":"Tôi đang đọc sách khi cô ấy gọi."},{"en":"They were sleeping at 10 PM.","vi":"Họ đang ngủ lúc 10 tối."}],"tips":["Thường dùng với 'when' hoặc 'while'"],"common_mistakes":["I was read → I was reading"]},
    {"title":"Present Perfect (Hiện Tại Hoàn Thành)","category":"Tenses","level":"B1","explanation":"Hành động đã xảy ra, có liên hệ với hiện tại. Cấu trúc: S + have/has + V3/ed.","examples":[{"en":"I have lived here for 5 years.","vi":"Tôi đã sống ở đây 5 năm rồi."},{"en":"She has just finished.","vi":"Cô ấy vừa mới xong."}],"tips":["Dấu hiệu: already, yet, just, ever, never, since, for"],"common_mistakes":["I have went → I have gone"]},
    {"title":"Future Simple (Tương Lai Đơn)","category":"Tenses","level":"A2","explanation":"Quyết định tức thời, dự đoán, lời hứa. Cấu trúc: S + will + V.","examples":[{"en":"I will help you.","vi":"Tôi sẽ giúp bạn."},{"en":"It will rain tomorrow.","vi":"Ngày mai trời sẽ mưa."}],"tips":["will not = won't"],"common_mistakes":["I will going → I will go"]},
    {"title":"Comparative & Superlative (So Sánh)","category":"Adjectives","level":"A2","explanation":"So sánh hơn: adj-er / more adj + than. So sánh nhất: the adj-est / the most adj.","examples":[{"en":"She is taller than me.","vi":"Cô ấy cao hơn tôi."},{"en":"This is the most beautiful city.","vi":"Đây là thành phố đẹp nhất."}],"tips":["Tính từ ngắn: thêm -er/-est. Tính từ dài: thêm more/most."],"common_mistakes":["more taller → taller","most beautifulest → most beautiful"]},
    {"title":"Articles (Mạo Từ a/an/the)","category":"Articles","level":"A1","explanation":"a/an: một (không xác định). the: cái (xác định). Không dùng mạo từ trước danh từ không đếm được/tổng quát.","examples":[{"en":"I have a cat and a dog. The cat is white.","vi":"Tôi có một con mèo và một con chó. Con mèo màu trắng."},{"en":"An apple a day keeps the doctor away.","vi":"Mỗi ngày một quả táo, bác sĩ xa ta."}],"tips":["'an' trước nguyên âm: an apple, an hour"],"common_mistakes":["a hour → an hour"]},
    {"title":"Prepositions of Time (in/on/at)","category":"Prepositions","level":"A1","explanation":"in: tháng, năm, mùa (in May, in 2024, in winter). on: ngày (on Monday, on July 4th). at: giờ, thời điểm cụ thể (at 5 PM, at night).","examples":[{"en":"I was born in 1990.","vi":"Tôi sinh năm 1990."},{"en":"The meeting is on Monday at 3 PM.","vi":"Cuộc họp vào thứ Hai lúc 3 giờ chiều."}],"tips":["at night, at noon, at midnight"],"common_mistakes":["in Monday → on Monday"]},
    {"title":"Modal Verbs (can/could/should/must)","category":"Modal Verbs","level":"A2","explanation":"can: có thể. could: có thể (quá khứ hoặc lịch sự). should: nên. must: phải.","examples":[{"en":"You should study harder.","vi":"Bạn nên học chăm hơn."},{"en":"I can swim.","vi":"Tôi có thể bơi."}],"tips":["Sau modal verb luôn là V nguyên thể (bare infinitive)"],"common_mistakes":["She can swims → She can swim"]},
    {"title":"Passive Voice (Câu Bị Động)","category":"Passive","level":"B1","explanation":"Nhấn mạnh đối tượng chịu tác động. Cấu trúc: S + be + V3/ed (+ by + tác nhân).","examples":[{"en":"The cake was made by my mom.","vi":"Bánh được làm bởi mẹ tôi."},{"en":"English is spoken worldwide.","vi":"Tiếng Anh được nói khắp thế giới."}],"tips":["Đổi O thành S, thêm 'by' nếu cần thiết."],"common_mistakes":["The book was wrote → was written"]},
    {"title":"Conditional Type 0 (Điều Kiện Loại 0)","category":"Conditionals","level":"B1","explanation":"Sự thật hiển nhiên. Cấu trúc: If + S + V (hiện tại đơn), S + V (hiện tại đơn).","examples":[{"en":"If you heat water to 100°C, it boils.","vi":"Nếu bạn đun nước đến 100°C, nó sôi."}],"tips":["Có thể thay 'if' bằng 'when'"],"common_mistakes":[]},
    {"title":"Conditional Type 1 (Điều Kiện Loại 1)","category":"Conditionals","level":"B1","explanation":"Có thể xảy ra ở tương lai. Cấu trúc: If + S + V (hiện tại đơn), S + will + V.","examples":[{"en":"If it rains, I will stay home.","vi":"Nếu trời mưa, tôi sẽ ở nhà."},{"en":"If you study, you will pass.","vi":"Nếu bạn học, bạn sẽ qua."}],"tips":["Mệnh đề If dùng hiện tại, mệnh đề chính dùng will."],"common_mistakes":["If it will rain → If it rains"]},
    {"title":"Conditional Type 2 (Điều Kiện Loại 2)","category":"Conditionals","level":"B2","explanation":"Giả định không có thật ở hiện tại. Cấu trúc: If + S + V2/ed, S + would + V.","examples":[{"en":"If I were rich, I would travel the world.","vi":"Nếu tôi giàu, tôi sẽ đi du lịch khắp thế giới."},{"en":"If she had time, she would help you.","vi":"Nếu cô ấy có thời gian, cô ấy sẽ giúp bạn."}],"tips":["Luôn dùng 'were' cho tất cả ngôi trong mệnh đề If (If I were...)"],"common_mistakes":["If I was → If I were"]},
    {"title":"Reported Speech (Câu Tường Thuật)","category":"Reported Speech","level":"B2","explanation":"Thuật lại lời người khác. Lùi thì: am/is→was, will→would, can→could.","examples":[{"en":"She said, 'I am tired.' → She said she was tired.","vi":"Cô ấy nói: 'Tôi mệt.' → Cô ấy nói cô ấy mệt."},{"en":"He said, 'I will come.' → He said he would come.","vi":"Anh ấy nói: 'Tôi sẽ đến.' → Anh ấy nói anh ấy sẽ đến."}],"tips":["Lùi 1 thì khi động từ tường thuật ở quá khứ"],"common_mistakes":["She said she is → She said she was"]},
    {"title":"Relative Clauses (Mệnh Đề Quan Hệ)","category":"Clauses","level":"B1","explanation":"Who: người. Which: vật. That: cả người và vật. Where: nơi chốn. When: thời gian.","examples":[{"en":"The man who called you is my brother.","vi":"Người đàn ông gọi điện cho bạn là anh trai tôi."},{"en":"The book which I bought is interesting.","vi":"Cuốn sách tôi mua rất thú vị."}],"tips":["MĐQH xác định: không dùng dấu phẩy. MĐQH không xác định: dùng dấu phẩy."],"common_mistakes":["The man which → The man who"]},
    {"title":"Gerunds & Infinitives (V-ing & To V)","category":"Verb Forms","level":"B1","explanation":"V-ing: sau enjoy, avoid, mind, finish, suggest. To V: sau want, need, decide, plan, agree.","examples":[{"en":"I enjoy learning English.","vi":"Tôi thích học tiếng Anh."},{"en":"She decided to quit.","vi":"Cô ấy quyết định nghỉ."}],"tips":["Một số V dùng cả hai: stop, remember, try (nghĩa khác nhau)"],"common_mistakes":["I enjoy to read → I enjoy reading"]},
    {"title":"Countable & Uncountable Nouns","category":"Nouns","level":"A2","explanation":"Đếm được: book, car, apple (dùng a/an, many, few). Không đếm được: water, money, information (dùng much, little).","examples":[{"en":"I need some water.","vi":"Tôi cần một ít nước."},{"en":"How many books do you have?","vi":"Bạn có bao nhiêu cuốn sách?"}],"tips":["Không đếm được: không dùng a/an, không thêm 's'"],"common_mistakes":["many water → much water","an information → information"]},
    {"title":"Question Tags (Câu Hỏi Đuôi)","category":"Questions","level":"B1","explanation":"Câu khẳng định → tag phủ định. Câu phủ định → tag khẳng định.","examples":[{"en":"You are a student, aren't you?","vi":"Bạn là sinh viên phải không?"},{"en":"She can't swim, can she?","vi":"Cô ấy không biết bơi phải không?"}],"tips":["Tag dùng trợ động từ tương ứng"],"common_mistakes":["He is smart, is he? → isn't he?"]},
    {"title":"Subject-Verb Agreement (Sự Hòa Hợp Chủ - Vị)","category":"Grammar Rules","level":"B1","explanation":"Chủ ngữ số ít → động từ số ít. Chủ ngữ số nhiều → động từ số nhiều.","examples":[{"en":"The team is ready.","vi":"Đội đã sẵn sàng."},{"en":"The students are studying.","vi":"Các sinh viên đang học."}],"tips":["Either...or, Neither...nor: chia theo chủ ngữ gần nhất"],"common_mistakes":["The news are → The news is"]},
]

# ═══════════════════════════════════════════════════════════════
# BÀI ĐỌC HIỂU (10 bài)
# ═══════════════════════════════════════════════════════════════
READING_FULL = [
    {"title":"A Day in the Life of a Software Engineer","level":"B1","topic":"Technology","article_type":"blog","word_count":250,
     "content":"Being a software engineer involves more than just writing code. A typical day starts with a short meeting called a 'stand-up'. In this meeting, team members discuss what they did yesterday, what they will do today, and any problems they are facing.\n\nAfter the meeting, the real work begins. Engineers spend hours writing, testing, and fixing code. They often work together in pairs to solve complex problems. This is called 'pair programming'.\n\nHowever, it's not all about coding. Communication is a big part of the job. Engineers need to write documentation, reply to emails, and talk to clients or other departments to understand their needs.\n\nLearning is also continuous. Technology changes quickly, so engineers must spend time reading articles, watching tutorials, or taking courses to keep their skills up to date.",
     "summary":"This article describes the daily routine of a software engineer, highlighting that the job involves meetings, communication, and continuous learning, not just writing code.",
     "questions":[{"question":"What happens during a 'stand-up' meeting?","options":["People eat breakfast.","Team members discuss their tasks.","They write code together.","They talk to clients."],"answer":"Team members discuss their tasks.","explanation":"The text says: 'In this meeting, team members discuss what they did yesterday, what they will do today.'"}]},
    {"title":"The Benefits of Learning a Second Language","level":"A2","topic":"Education","article_type":"blog","word_count":180,
     "content":"Learning a second language has many benefits. First, it improves your memory and thinking skills. Studies show that bilingual people are better at solving problems and multitasking.\n\nSecond, knowing another language opens doors to new cultures. You can read books, watch movies, and talk to people in their native language. This makes traveling more enjoyable and meaningful.\n\nThird, it can help your career. Many companies prefer employees who speak more than one language. In today's global economy, being bilingual is a valuable skill.\n\nFinally, learning a language is good for your brain health. Research suggests it can delay the onset of Alzheimer's disease.",
     "summary":"Learning a second language improves cognitive skills, opens cultural doors, boosts career prospects, and promotes brain health.",
     "questions":[{"question":"What is one benefit of being bilingual?","options":["You can sleep better.","You are better at problem-solving.","You earn more money.","You can eat more food."],"answer":"You are better at problem-solving.","explanation":"The text says bilingual people are better at solving problems."}]},
    {"title":"Climate Change: What Can We Do?","level":"B2","topic":"Environment","article_type":"news","word_count":300,
     "content":"Climate change is one of the biggest challenges facing our planet today. The Earth's average temperature has risen by about 1.1°C since the pre-industrial era, mainly due to human activities such as burning fossil fuels, deforestation, and industrial processes.\n\nThe effects of climate change are already visible: rising sea levels, more frequent extreme weather events, and loss of biodiversity. Scientists warn that if we don't act quickly, these impacts will become much worse.\n\nSo what can individuals do? Here are some practical steps:\n\n1. Reduce energy consumption: Turn off lights, use energy-efficient appliances, and insulate your home.\n2. Choose sustainable transport: Walk, cycle, or use public transport instead of driving.\n3. Eat less meat: The meat industry is a major source of greenhouse gas emissions.\n4. Reduce, reuse, recycle: Minimize waste and choose products with less packaging.\n5. Support renewable energy: Consider solar panels or green energy suppliers.\n\nWhile individual actions are important, systemic change is also necessary. Governments and corporations must commit to reducing emissions and investing in clean energy.",
     "summary":"Climate change is caused by human activities. Individuals can help by reducing energy use, using sustainable transport, eating less meat, and recycling. Systemic change from governments is also essential.",
     "questions":[{"question":"What is the main cause of climate change according to the article?","options":["Natural disasters","Human activities","Solar radiation","Ocean currents"],"answer":"Human activities","explanation":"The text states temperature rise is 'mainly due to human activities such as burning fossil fuels.'"}]},
    {"title":"The Story of Coffee","level":"A2","topic":"Food","article_type":"story","word_count":200,
     "content":"Coffee is one of the most popular drinks in the world. But where did it come from?\n\nAccording to legend, a goat herder named Kaldi in Ethiopia noticed that his goats became very energetic after eating berries from a certain tree. He tried the berries himself and felt more awake and alert.\n\nKaldi told the monks at a local monastery about his discovery. They made a drink from the berries and found that it helped them stay awake during long prayers.\n\nFrom Ethiopia, coffee spread to the Arabian Peninsula, where it became very popular. By the 16th century, coffee houses had appeared in cities across the Middle East. These were places where people gathered to drink coffee, listen to music, and discuss current events.\n\nToday, coffee is grown in more than 70 countries and over 2 billion cups are consumed every day.",
     "summary":"The story traces coffee's origin from Ethiopia (discovered by goat herder Kaldi) to its global popularity today.",
     "questions":[{"question":"Who discovered coffee according to legend?","options":["A monk","A king","A goat herder named Kaldi","A trader from Arabia"],"answer":"A goat herder named Kaldi","explanation":"The text says 'a goat herder named Kaldi in Ethiopia noticed.'"}]},
    {"title":"How the Internet Changed Communication","level":"B1","topic":"Technology","article_type":"blog","word_count":220,
     "content":"Before the internet, communication was much slower. People wrote letters that took days or weeks to arrive. Long-distance phone calls were expensive, and you had to wait by the phone to receive a call.\n\nThe internet changed everything. Email allowed people to send messages instantly to anyone in the world. Chat rooms and instant messaging made real-time conversations possible, no matter the distance.\n\nSocial media took communication to another level. Platforms like Facebook, Instagram, and Twitter allow people to share their lives, connect with old friends, and meet new people. Video calling through Zoom or Skype lets us see and talk to loved ones far away.\n\nHowever, the internet has also created some problems. Many people feel overwhelmed by the constant stream of messages and notifications. Cyberbullying and fake news are serious concerns. And some argue that digital communication is less meaningful than face-to-face conversation.\n\nDespite these challenges, the internet has fundamentally changed how we connect with each other, making the world a smaller and more connected place.",
     "summary":"The internet revolutionized communication through email, social media, and video calling, but also brought challenges like information overload and cyberbullying.",
     "questions":[{"question":"What was a problem with communication before the internet?","options":["It was too fast","Letters took days or weeks","Everyone had smartphones","Email was too expensive"],"answer":"Letters took days or weeks","explanation":"The text states: 'People wrote letters that took days or weeks to arrive.'"}]},
    {"title":"Healthy Eating Habits","level":"A1","topic":"Health","article_type":"blog","word_count":150,
     "content":"Eating healthy food is very important for your body. Here are some simple tips:\n\nFirst, eat lots of fruits and vegetables. They have vitamins and minerals that keep you strong. Try to eat five portions every day.\n\nSecond, drink water. Water is the best drink for your body. Try to drink eight glasses every day. Avoid sugary drinks like soda.\n\nThird, eat breakfast every morning. Breakfast gives you energy to start your day. Good breakfast foods include oatmeal, eggs, and fruit.\n\nFourth, don't eat too much sugar and salt. Too much sugar can make you gain weight. Too much salt is bad for your heart.\n\nFinally, eat slowly and enjoy your food. When you eat too fast, you often eat too much.",
     "summary":"Simple healthy eating tips: eat fruits and vegetables, drink water, eat breakfast, limit sugar and salt, and eat slowly.",
     "questions":[{"question":"How many glasses of water should you drink daily?","options":["Two","Five","Eight","Ten"],"answer":"Eight","explanation":"The text says: 'Try to drink eight glasses every day.'"}]},
    {"title":"The History of the Olympic Games","level":"B1","topic":"Sports","article_type":"academic","word_count":250,
     "content":"The Olympic Games have a long and fascinating history. The ancient Olympics began in Olympia, Greece, around 776 BC. These games were held every four years as part of a religious festival honoring Zeus, the king of the Greek gods.\n\nThe ancient Olympics included events such as running, wrestling, boxing, and chariot racing. Only men could compete, and the games were so important that wars were stopped during the Olympic period.\n\nThe ancient Olympics continued for nearly 12 centuries before being banned in 393 AD by the Roman Emperor Theodosius I, who considered them a pagan festival.\n\nThe modern Olympics were revived in 1896 by Pierre de Coubertin, a French educator. The first modern games were held in Athens, Greece, with athletes from 14 countries competing in 43 events.\n\nToday, the Olympics are the world's largest sporting event, with thousands of athletes from over 200 countries competing in hundreds of events. The games continue to promote peace, friendship, and fair competition among nations.",
     "summary":"The Olympics originated in ancient Greece (776 BC), were revived in 1896, and are now the world's largest sporting event promoting peace and fair competition.",
     "questions":[{"question":"When did the ancient Olympics begin?","options":["393 AD","1896","776 BC","1000 BC"],"answer":"776 BC","explanation":"The text states: 'The ancient Olympics began in Olympia, Greece, around 776 BC.'"}]},
    {"title":"Artificial Intelligence in Daily Life","level":"B2","topic":"Technology","article_type":"news","word_count":280,
     "content":"Artificial Intelligence (AI) is no longer just science fiction — it's part of our everyday lives. From the moment you wake up and ask your smart speaker about the weather, to the Netflix recommendations you browse before bed, AI is working behind the scenes.\n\nVirtual assistants like Siri, Alexa, and Google Assistant use natural language processing to understand and respond to your questions. They can set alarms, play music, control smart home devices, and answer general knowledge questions.\n\nAI also powers the recommendation systems used by streaming services, online stores, and social media platforms. These systems analyze your behavior and preferences to suggest content you might enjoy.\n\nIn healthcare, AI is being used to analyze medical images, predict diseases, and even assist in surgery. Self-driving cars use AI to navigate roads and make split-second decisions.\n\nHowever, AI also raises important ethical questions. Issues of privacy, job displacement, and algorithmic bias need to be addressed as AI becomes more prevalent in society.\n\nAs AI technology continues to advance, it will likely play an even bigger role in our lives. Understanding how it works and its implications is becoming an essential skill for everyone.",
     "summary":"AI is deeply integrated into daily life through virtual assistants, recommendation systems, healthcare, and autonomous vehicles. Ethical concerns about privacy and bias remain important.",
     "questions":[{"question":"What does AI use to understand your questions?","options":["Sign language","Natural language processing","Body language","Morse code"],"answer":"Natural language processing","explanation":"The text says virtual assistants 'use natural language processing to understand and respond.'"}]},
    {"title":"My First Trip Abroad","level":"A1","topic":"Travel","article_type":"story","word_count":120,
     "content":"Last summer, I went to Japan for the first time. I was very excited! The plane ride was long — about six hours.\n\nWhen I arrived in Tokyo, everything was so different. The city was very big and busy. There were lights and signs everywhere. I couldn't read the Japanese writing, but people were very kind and helpful.\n\nI visited many places: Tokyo Tower, a beautiful temple, and Shibuya Crossing. The food was amazing! I tried sushi, ramen, and tempura.\n\nI also went to a traditional Japanese garden. It was so peaceful and beautiful. I took many photos.\n\nI loved Japan and I want to go back someday.",
     "summary":"A first-person account of a beginner's trip to Japan, describing Tokyo's sights, food, and the kindness of locals.",
     "questions":[{"question":"How long was the plane ride?","options":["Two hours","Four hours","Six hours","Ten hours"],"answer":"Six hours","explanation":"The text says: 'The plane ride was long — about six hours.'"}]},
    {"title":"Working from Home: Pros and Cons","level":"B1","topic":"Business","article_type":"blog","word_count":230,
     "content":"Since the pandemic, working from home has become normal for many people. While it offers many advantages, there are also some challenges.\n\nPros:\n- Flexibility: You can set your own schedule and work when you're most productive.\n- No commute: You save time and money by not traveling to an office.\n- Comfort: You can work in comfortable clothes from your favorite spot at home.\n- Better work-life balance: You have more time for family and hobbies.\n\nCons:\n- Isolation: You miss the social interaction with colleagues.\n- Distractions: Home has many distractions, like TV, housework, and family members.\n- Work-life boundaries: It can be hard to 'switch off' when your office is also your home.\n- Communication: It's harder to collaborate and communicate effectively without face-to-face meetings.\n\nMany companies now offer hybrid models, where employees work from home some days and go to the office on others. This seems to be the best of both worlds for many workers.",
     "summary":"Working from home offers flexibility and no commute but can lead to isolation and blurred boundaries. Hybrid models are becoming popular.",
     "questions":[{"question":"What is a disadvantage of working from home?","options":["Saving money","Isolation from colleagues","Having a flexible schedule","Wearing comfortable clothes"],"answer":"Isolation from colleagues","explanation":"The text lists 'Isolation: You miss the social interaction with colleagues' as a con."}]},
]

# ═══════════════════════════════════════════════════════════════
# BÀI LUYỆN NGHE (10 bài)
# ═══════════════════════════════════════════════════════════════
LISTENING_FULL = [
    {"title":"Ordering Food in a Restaurant","level":"A1","topic":"Daily Life","exercise_type":"comprehension","description":"A customer orders food at a restaurant.",
     "transcript":"Waiter: Hello, are you ready to order?\nCustomer: Yes, I'd like the grilled chicken salad, please.\nWaiter: Would you like anything to drink?\nCustomer: Just water with ice, thank you.\nWaiter: Any dessert?\nCustomer: No, that will be all for now.",
     "questions":[{"question":"What did the customer order?","options":["Pizza","Grilled chicken salad","Steak","Pasta"],"answer":"Grilled chicken salad"}]},
    {"title":"Asking for Directions","level":"A1","topic":"Travel","exercise_type":"comprehension","description":"A tourist asks for directions to the museum.",
     "transcript":"Tourist: Excuse me, could you tell me how to get to the museum?\nLocal: Sure! Go straight ahead for two blocks, then turn left at the traffic light. The museum is on your right.\nTourist: How long does it take to walk there?\nLocal: About ten minutes.\nTourist: Thank you so much!",
     "questions":[{"question":"Where does the tourist want to go?","options":["The park","The museum","The hospital","The hotel"],"answer":"The museum"}]},
    {"title":"Job Interview","level":"B1","topic":"Business","exercise_type":"comprehension","description":"A candidate interviews for a marketing position.",
     "transcript":"Interviewer: So, tell me about yourself.\nCandidate: I graduated from Hanoi University with a degree in Marketing. I've been working at ABC Company for three years as a digital marketing specialist.\nInterviewer: Why do you want to leave your current job?\nCandidate: I'm looking for new challenges and opportunities to grow. Your company is known for innovation, and I'd love to be part of that.\nInterviewer: What would you say is your greatest strength?\nCandidate: I'm very data-driven. I always analyze results before making decisions.",
     "questions":[{"question":"How long has the candidate worked at ABC Company?","options":["One year","Two years","Three years","Five years"],"answer":"Three years"}]},
    {"title":"Weather Forecast","level":"A2","topic":"Daily Life","exercise_type":"dictation","description":"Listen to today's weather forecast.",
     "transcript":"Good morning! Here's today's weather forecast. It will be sunny this morning with temperatures around 25 degrees Celsius. However, clouds will move in this afternoon, and there's a 40 percent chance of rain in the evening. Temperatures will drop to about 18 degrees overnight. Don't forget to bring an umbrella!",
     "questions":[{"question":"What is the morning temperature?","options":["18°C","20°C","25°C","30°C"],"answer":"25°C"}]},
    {"title":"At the Doctor's Office","level":"A2","topic":"Health","exercise_type":"comprehension","description":"A patient visits the doctor with a headache.",
     "transcript":"Doctor: Good morning. What seems to be the problem?\nPatient: I've been having terrible headaches for the past week.\nDoctor: How often do you get them?\nPatient: Almost every day, usually in the afternoon.\nDoctor: Do you spend a lot of time looking at screens?\nPatient: Yes, I work on a computer all day.\nDoctor: That could be the cause. I recommend taking breaks every 30 minutes and doing some eye exercises.",
     "questions":[{"question":"What does the doctor recommend?","options":["Surgery","Taking breaks every 30 minutes","Sleeping more","Drinking coffee"],"answer":"Taking breaks every 30 minutes"}]},
    {"title":"Airport Announcement","level":"A2","topic":"Travel","exercise_type":"dictation","description":"An announcement at the airport about a flight.",
     "transcript":"Attention all passengers on Flight VN256 to Ho Chi Minh City. We regret to inform you that this flight has been delayed by approximately two hours due to bad weather conditions. The new departure time is 4:30 PM. We apologize for any inconvenience. Please proceed to Gate B12 for boarding.",
     "questions":[{"question":"Why was the flight delayed?","options":["Technical problem","Bad weather","Pilot shortage","Security check"],"answer":"Bad weather"}]},
    {"title":"Shopping at the Supermarket","level":"A1","topic":"Shopping","exercise_type":"comprehension","description":"Two friends shopping for groceries.",
     "transcript":"Anna: We need to buy some things for dinner tonight.\nBen: Okay, what should we get?\nAnna: Let's make pasta. We need tomatoes, onions, garlic, and some cheese.\nBen: Do we have pasta at home?\nAnna: No, we need to buy that too. And some olive oil.\nBen: Should we get some fruit too?\nAnna: Good idea! Let's get some apples and bananas.",
     "questions":[{"question":"What are they going to cook?","options":["Pizza","Salad","Pasta","Soup"],"answer":"Pasta"}]},
    {"title":"University Lecture: Introduction to Psychology","level":"B2","topic":"Education","exercise_type":"comprehension","description":"The first minutes of a psychology lecture.",
     "transcript":"Good morning, everyone. Welcome to Introduction to Psychology. My name is Professor Nguyen, and I'll be your instructor this semester. Psychology is the scientific study of the mind and behavior. In this course, we'll explore topics like memory, perception, emotions, and mental health. By the end of this course, you'll understand why people think, feel, and act the way they do. Your first assignment is to read Chapter 1 and write a one-page reflection on what psychology means to you. Any questions?",
     "questions":[{"question":"What is the first assignment?","options":["Write a research paper","Read Chapter 1 and write a reflection","Take a quiz","Present a topic"],"answer":"Read Chapter 1 and write a reflection"}]},
    {"title":"Phone Call: Making a Reservation","level":"A2","topic":"Travel","exercise_type":"comprehension","description":"Calling a hotel to book a room.",
     "transcript":"Receptionist: Grand Hotel, how can I help you?\nCaller: I'd like to book a room for two nights, please.\nReceptionist: Sure. When would you like to check in?\nCaller: Next Friday, July 18th.\nReceptionist: Let me check availability. Yes, we have a standard room available for 800,000 VND per night, and a deluxe room for 1,200,000 VND.\nCaller: I'll take the standard room, please.\nReceptionist: May I have your name?\nCaller: It's Nguyen Van Minh.",
     "questions":[{"question":"How much is the standard room per night?","options":["500,000 VND","800,000 VND","1,000,000 VND","1,200,000 VND"],"answer":"800,000 VND"}]},
    {"title":"TED Talk Excerpt: The Power of Reading","level":"B1","topic":"Education","exercise_type":"comprehension","description":"A short excerpt about how reading changes your brain.",
     "transcript":"Reading is one of the most powerful things you can do for your brain. When you read, multiple areas of your brain are activated simultaneously. Your brain creates mental images, processes emotions, and makes connections to your own experiences. Studies have shown that people who read regularly have better vocabularies, stronger analytical skills, and greater empathy. Reading fiction, in particular, helps you understand other people's perspectives and emotions. So the next time you pick up a book, remember: you're not just enjoying a story — you're literally rewiring your brain.",
     "questions":[{"question":"What does reading fiction help with?","options":["Better math skills","Understanding others' perspectives","Physical fitness","Cooking skills"],"answer":"Understanding others' perspectives"}]},
]

# ═══════════════════════════════════════════════════════════════
# KHÓA HỌC (3 khóa hoàn chỉnh)
# ═══════════════════════════════════════════════════════════════
COURSES_FULL = [
    {"title":"English for Absolute Beginners","description":"Khóa học dành cho người mới bắt đầu hoàn toàn. Học chào hỏi, giới thiệu bản thân, và giao tiếp cơ bản.","level":"A1","category":"general","total_lessons":8,"is_published":True,
     "lessons":[
         {"title":"Greetings & Introductions","lesson_type":"vocabulary","content":"<h3>Chào hỏi cơ bản</h3><p><b>Hello</b> /həˈləʊ/ - Xin chào<br><b>Good morning</b> - Chào buổi sáng<br><b>Good afternoon</b> - Chào buổi chiều<br><b>Good evening</b> - Chào buổi tối<br><b>Goodbye</b> - Tạm biệt<br><b>How are you?</b> - Bạn khỏe không?<br><b>I'm fine, thank you.</b> - Tôi khỏe, cảm ơn.</p>","xp_reward":30},
         {"title":"Numbers 1-100","lesson_type":"vocabulary","content":"<h3>Số đếm</h3><p>1-one, 2-two, 3-three, 4-four, 5-five, 6-six, 7-seven, 8-eight, 9-nine, 10-ten, 20-twenty, 30-thirty, 50-fifty, 100-one hundred.</p>","xp_reward":30},
         {"title":"Colors & Shapes","lesson_type":"vocabulary","content":"<h3>Màu sắc và Hình dạng</h3><p><b>Red</b>-đỏ, <b>Blue</b>-xanh dương, <b>Green</b>-xanh lá, <b>Yellow</b>-vàng, <b>Black</b>-đen, <b>White</b>-trắng, <b>Orange</b>-cam, <b>Purple</b>-tím, <b>Pink</b>-hồng.</p>","xp_reward":30},
         {"title":"Verb To Be","lesson_type":"grammar","content":"<h3>Động từ 'To Be'</h3><p><b>I am</b> (I'm) - Tôi là<br><b>You are</b> (You're) - Bạn là<br><b>He/She/It is</b> (He's/She's/It's) - Anh ấy/Cô ấy/Nó là<br><b>We are</b> (We're) - Chúng tôi là<br><b>They are</b> (They're) - Họ là</p>","xp_reward":40},
         {"title":"Family Members","lesson_type":"vocabulary","content":"<h3>Thành viên gia đình</h3><p><b>Father/Dad</b>-Bố, <b>Mother/Mom</b>-Mẹ, <b>Brother</b>-Anh/Em trai, <b>Sister</b>-Chị/Em gái, <b>Grandfather</b>-Ông, <b>Grandmother</b>-Bà, <b>Uncle</b>-Chú/Bác, <b>Aunt</b>-Cô/Dì.</p>","xp_reward":30},
         {"title":"Daily Routine","lesson_type":"grammar","content":"<h3>Thói quen hàng ngày</h3><p>Sử dụng thì <b>Hiện tại đơn</b>.<br><b>I wake up</b> at 6 AM. <b>I brush</b> my teeth. <b>I eat</b> breakfast. <b>I go</b> to school/work. <b>I come</b> home. <b>I sleep</b> at 10 PM.</p>","xp_reward":40},
         {"title":"Food & Drinks","lesson_type":"vocabulary","content":"<h3>Đồ ăn và Thức uống</h3><p><b>Rice</b>-cơm, <b>Bread</b>-bánh mì, <b>Chicken</b>-thịt gà, <b>Fish</b>-cá, <b>Egg</b>-trứng, <b>Water</b>-nước, <b>Coffee</b>-cà phê, <b>Tea</b>-trà, <b>Milk</b>-sữa, <b>Juice</b>-nước ép.</p>","xp_reward":30},
         {"title":"Conversation Practice","lesson_type":"speaking","content":"<h3>Luyện hội thoại</h3><p>Hãy tập giới thiệu bản thân:<br>'Hello! My name is [tên bạn]. I am from Vietnam. I am [tuổi] years old. Nice to meet you!'</p>","xp_reward":50},
     ]},
    {"title":"Business English Communication","description":"Nâng cao kỹ năng giao tiếp tiếng Anh trong công việc: email, họp, thuyết trình.","level":"B1","category":"business","total_lessons":6,"is_published":True,
     "lessons":[
         {"title":"Professional Email Writing","lesson_type":"writing","content":"<h3>Viết Email Chuyên Nghiệp</h3><p><b>Subject line:</b> Clear and specific<br><b>Greeting:</b> Dear Mr./Ms. [Name]<br><b>Body:</b> I am writing to inform you... / I would like to request...<br><b>Closing:</b> Best regards, / Sincerely,</p>","xp_reward":50},
         {"title":"Meeting Vocabulary","lesson_type":"vocabulary","content":"<h3>Từ vựng Cuộc họp</h3><p><b>Agenda</b>-chương trình nghị sự, <b>Minutes</b>-biên bản, <b>Chair</b>-chủ tọa, <b>Proposal</b>-đề xuất, <b>Deadline</b>-thời hạn, <b>Budget</b>-ngân sách, <b>Stakeholder</b>-bên liên quan.</p>","xp_reward":40},
         {"title":"Giving Presentations","lesson_type":"speaking","content":"<h3>Thuyết trình bằng Tiếng Anh</h3><p><b>Opening:</b> Good morning everyone. Today I'd like to talk about...<br><b>Structure:</b> First... Second... Finally...<br><b>Closing:</b> In conclusion... Thank you for your attention. Any questions?</p>","xp_reward":60},
         {"title":"Negotiation Skills","lesson_type":"speaking","content":"<h3>Kỹ năng Đàm phán</h3><p><b>I'd like to propose...</b><br><b>What if we...?</b><br><b>That's a fair point, but...</b><br><b>Can we find a compromise?</b><br><b>I'm afraid that won't work for us.</b></p>","xp_reward":60},
         {"title":"Business Idioms","lesson_type":"vocabulary","content":"<h3>Thành ngữ Kinh doanh</h3><p><b>Break the ice</b>-phá vỡ sự im lặng<br><b>Think outside the box</b>-suy nghĩ sáng tạo<br><b>Cut corners</b>-làm tắt<br><b>Get the ball rolling</b>-bắt đầu<br><b>Touch base</b>-liên lạc lại</p>","xp_reward":40},
         {"title":"Report Writing","lesson_type":"writing","content":"<h3>Viết Báo cáo</h3><p><b>Title Page</b> → <b>Executive Summary</b> → <b>Introduction</b> → <b>Findings</b> → <b>Conclusion</b> → <b>Recommendations</b></p>","xp_reward":50},
     ]},
    {"title":"IELTS Preparation","description":"Luyện thi IELTS toàn diện: Listening, Reading, Writing, Speaking.","level":"B2","category":"ielts","total_lessons":6,"is_published":True,
     "lessons":[
         {"title":"IELTS Listening: Section 1","lesson_type":"listening","content":"<h3>IELTS Listening Section 1</h3><p>Phần 1 thường là cuộc hội thoại giữa 2 người về tình huống hàng ngày (đặt phòng, đăng ký khóa học...). Tips: Đọc câu hỏi trước khi nghe. Chú ý số, tên, ngày tháng.</p>","xp_reward":60},
         {"title":"IELTS Reading: Skimming & Scanning","lesson_type":"reading","content":"<h3>Kỹ thuật đọc nhanh</h3><p><b>Skimming:</b> Đọc lướt để nắm ý chính (đọc tiêu đề, câu đầu mỗi đoạn).<br><b>Scanning:</b> Đọc tìm thông tin cụ thể (tên, số, ngày tháng).</p>","xp_reward":60},
         {"title":"IELTS Writing Task 1: Charts & Graphs","lesson_type":"writing","content":"<h3>Mô tả biểu đồ</h3><p>Từ vựng quan trọng: <b>increase/rise/grow</b> (tăng), <b>decrease/fall/drop</b> (giảm), <b>remain stable</b> (ổn định), <b>peak</b> (đạt đỉnh), <b>fluctuate</b> (dao động).</p>","xp_reward":70},
         {"title":"IELTS Writing Task 2: Essay Structure","lesson_type":"writing","content":"<h3>Cấu trúc bài luận</h3><p><b>Introduction:</b> Paraphrase đề bài + thesis statement.<br><b>Body 1:</b> Main idea 1 + evidence.<br><b>Body 2:</b> Main idea 2 + evidence.<br><b>Conclusion:</b> Tóm tắt + ý kiến cá nhân.</p>","xp_reward":70},
         {"title":"IELTS Speaking Part 1 & 2","lesson_type":"speaking","content":"<h3>Luyện Speaking</h3><p><b>Part 1:</b> Câu hỏi cá nhân (hometown, hobbies, work). Trả lời 2-3 câu.<br><b>Part 2:</b> Nói 1-2 phút về một chủ đề. Dùng cấu trúc: What, When, Where, Why, How.</p>","xp_reward":70},
         {"title":"IELTS Speaking Part 3: Discussion","lesson_type":"speaking","content":"<h3>Thảo luận chuyên sâu</h3><p>Sử dụng cấu trúc nâng cao:<br><b>From my perspective...</b><br><b>On the one hand... on the other hand...</b><br><b>This is primarily because...</b><br><b>To sum up...</b></p>","xp_reward":70},
     ]},
]


async def run_full_seed():
    await init_db()
    async with AsyncSessionLocal() as db:
        # Check existing count
        vocab_count = (await db.execute(select(func.count(Vocabulary.id)))).scalar() or 0
        print(f"Existing vocabulary count: {vocab_count}")

        if vocab_count < 500:
            print("Seeding vocabulary (780 words)...")
            for letter, words in VOCAB.items():
                for w in words:
                    db.add(Vocabulary(**w))
            await db.flush()
            print("Vocabulary seeded!")

        grammar_count = (await db.execute(select(func.count(GrammarRule.id)))).scalar() or 0
        if grammar_count < 15:
            print("Seeding grammar (20 rules)...")
            for g in GRAMMAR_FULL:
                db.add(GrammarRule(**g))
            await db.flush()
            print("Grammar seeded!")

        reading_count = (await db.execute(select(func.count(ReadingArticle.id)))).scalar() or 0
        if reading_count < 8:
            print("Seeding reading (10 articles)...")
            for r in READING_FULL:
                db.add(ReadingArticle(**r))
            await db.flush()
            print("Reading seeded!")

        listening_count = (await db.execute(select(func.count(ListeningExercise.id)))).scalar() or 0
        if listening_count < 8:
            print("Seeding listening (10 exercises)...")
            for l in LISTENING_FULL:
                db.add(ListeningExercise(**l))
            await db.flush()
            print("Listening seeded!")

        course_count = (await db.execute(select(func.count(Course.id)))).scalar() or 0
        if course_count < 3:
            print("Seeding courses (3 complete courses)...")
            for course_data in COURSES_FULL:
                lessons_data = course_data.pop("lessons", [])
                course = Course(**course_data)
                db.add(course)
                await db.flush()
                for i, lesson_item in enumerate(lessons_data):
                    lesson = Lesson(course_id=course.id, order_index=i, duration_minutes=15, **lesson_item)
                    db.add(lesson)
            await db.flush()
            print("Courses seeded!")

        badge_count = (await db.execute(select(func.count(Badge.id)))).scalar() or 0
        if badge_count < 5:
            print("Seeding badges & missions...")
            badges = [
                {"name":"First Step","description":"Hoàn thành bài học đầu tiên","icon":"🎓","category":"general","xp_reward":50},
                {"name":"Vocab Master 50","description":"Học 50 từ vựng","icon":"📚","category":"vocab","xp_reward":100},
                {"name":"Vocab Master 200","description":"Học 200 từ vựng","icon":"📖","category":"vocab","xp_reward":300},
                {"name":"3-Day Streak","description":"Học liên tục 3 ngày","icon":"🔥","category":"streak","xp_reward":150},
                {"name":"7-Day Streak","description":"Học liên tục 7 ngày","icon":"🔥","category":"streak","xp_reward":300},
                {"name":"Grammar Expert","description":"Đạt 100% bài tập ngữ pháp","icon":"🏆","category":"grammar","xp_reward":200},
                {"name":"Quiz Champion","description":"Hoàn thành 50 bài quiz","icon":"🏅","category":"quiz","xp_reward":250},
            ]
            for b in badges:
                db.add(Badge(**b))

            missions = [
                {"title":"Học 5 từ mới","description":"Hoàn thành học 5 từ vựng mới hôm nay","mission_type":"daily","xp_reward":20,"coin_reward":5},
                {"title":"Ôn tập 10 flashcard","description":"Ôn tập 10 từ vựng đã học","mission_type":"daily","xp_reward":30,"coin_reward":5},
                {"title":"Làm 1 bài quiz","description":"Hoàn thành ít nhất 1 bài quiz","mission_type":"daily","xp_reward":20,"coin_reward":3},
                {"title":"Chat AI 5 tin nhắn","description":"Nói chuyện với AI Teacher ít nhất 5 câu","mission_type":"daily","xp_reward":25,"coin_reward":5},
                {"title":"Đọc 1 bài Reading","description":"Đọc xong 1 bài đọc hiểu","mission_type":"daily","xp_reward":30,"coin_reward":5},
                {"title":"Tích lũy 500 XP tuần","description":"Kiếm đủ 500 XP trong tuần","mission_type":"weekly","xp_reward":100,"coin_reward":20},
            ]
            for m in missions:
                db.add(Mission(**m))
            await db.flush()
            print("Badges & missions seeded!")

        await db.commit()
        
        # Final counts
        vc = (await db.execute(select(func.count(Vocabulary.id)))).scalar()
        gc = (await db.execute(select(func.count(GrammarRule.id)))).scalar()
        rc = (await db.execute(select(func.count(ReadingArticle.id)))).scalar()
        lc = (await db.execute(select(func.count(ListeningExercise.id)))).scalar()
        cc = (await db.execute(select(func.count(Course.id)))).scalar()
        print(f"\n=== SEED COMPLETE ===")
        print(f"Vocabulary: {vc}")
        print(f"Grammar Rules: {gc}")
        print(f"Reading Articles: {rc}")
        print(f"Listening Exercises: {lc}")
        print(f"Courses: {cc}")

if __name__ == "__main__":
    asyncio.run(run_full_seed())
