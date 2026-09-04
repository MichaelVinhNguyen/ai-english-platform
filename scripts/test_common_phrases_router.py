import asyncio
import sys
sys.stdout.reconfigure(encoding='utf-8')
from backend.routers.common_phrases import get_topics, get_topic_phrases, search_phrases

async def main():
    t_res = await get_topics()
    print(f"Total topics returned: {len(t_res['topics'])}")
    print(f"Topic #1: {t_res['topics'][0]['title']} ({t_res['topics'][0]['title_vi']})")

    p_res = await get_topic_phrases(1)
    print(f"Topic #1 phrase count: {len(p_res['phrases'])}")
    p1 = p_res['phrases'][0]
    print(f"Q1: {p1['q_text']} [{p1['q_ipa']}] -> {p1['q_vi']}")
    print(f"A1: {p1['a_text']} [{p1['a_ipa']}] -> {p1['a_vi']}")
    print(f"Tip: {p1['tips']}")
    print(f"Vocab: {p1['key_vocab']}")

    s_res = await search_phrases('meeting')
    print(f"Search 'meeting' results count: {len(s_res['results'])}")
    if s_res['results']:
        print(f"Match #1: {s_res['results'][0]['q_text']} ({s_res['results'][0]['topic_title']})")

if __name__ == '__main__':
    asyncio.run(main())
