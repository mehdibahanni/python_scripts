import requests
import m3u8
from urllib.parse import urljoin
import os

# # you most install 'ffmpeg' tool,
# to ensur that you can convert segment to file with extension of .mp4
# subprocess.run[('ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'segments.txt', '-c', 'copy', 'output.mp4')]

# عنوان URL الرئيسي لملف M3U8
master_url = 'https://spe.mwdy.club/hls/,uncltkgslcrt55h3jyzbtw53ey3tvxnqd6or7xzgxocs6exupq2tqr7qc74q,.urlset/master.m3u8'


# إرسال طلب GET لجلب محتوى ملف M3U8 الرئيسي
r = requests.get(master_url)
m3u8_master = m3u8.loads(r.text)

# استخراج روابط الحلقات من ملف M3U8 الرئيسي
for playlist in m3u8_master.data['playlists']:
    uri = playlist['uri']
    full_uri = urljoin(master_url, uri)
    # print(full_uri)  # طباعة الرابط الكامل للحلقة
    
    # إرسال طلب GET لجلب محتوى قائمة التشغيل
    play_r = requests.get(full_uri)
    m3u8_playlist = m3u8.loads(play_r.text)

    # استخراج روابط الأجزاء داخل قائمة التشغيل
    with open('segments.txt', 'w') as file:
        for segment in m3u8_playlist.data['segments']:
            segment_uri = segment['uri']
            full_segment_uri = urljoin(full_uri, segment_uri)
            file.write(f"file '{full_segment_uri}'\n")








        # print(full_segment_uri)  # طباعة الرابط الكامل للجزء

        # for i, url in enumerate(full_segment_uri):
        #     response = requests.get(url)
        #     with open(f'segment_{i}.ts', 'wb') as file:
        #         file.write(response.content)
        #     print(f'Segment {i} downloaded')


        # # التحقق مما إذا كانت الروابط بتنسيق MP4
        # if full_segment_uri.endswith('.mp4'):
        #     print(f'MP4 segment found: {full_segment_uri}')