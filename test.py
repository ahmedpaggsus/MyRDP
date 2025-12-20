import requests, cloudscraper, time, json, os, random, backoff, yt_dlp, sys, subprocess
from fake_useragent import UserAgent
from tqdm import tqdm
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# ==========================================================
# 👑 THE ARCHIVAL FUSION REACTOR - VERSION 25.0 [ULTIMATE]
# ==========================================================
# OWNER: SOVEREIGN ARCHIVIST
# TARGET: @drFathysaid (TOTAL DOMINANCE)
# FEATURES: LIVE, SHORTS, PODCASTS, PIXEL-PERFECTION
# ==========================================================

class SovereignFusionReactor:
    def __init__(self):
        self.ua = UserAgent()
        self.scraper = cloudscraper.create_scraper(
            browser={'browser': 'chrome', 'platform': 'windows', 'desktop': True}
        )
        self.auth = "LOW 0QXWMqn3plltxkHY:EBZOMdJmS6WKfCzp"
        self.input_file = "dr_fathy_ALL_links_oldest_to_newest.txt"
        self.vault_file = "TOTAL_IMMORTALITY_VAULT_V25.json"
        self.error_log = "reactor_errors.log"
        self.cookies_file = "cookies.txt"
        self.setup_environment()

    def setup_environment(self):
        """تجهيز بيئة العمل والتحقق من الملفات"""
        print(f"🚀 [SYSTEM] BOOTING REACTOR V25.0 AT {datetime.now()}")
        if not os.path.exists(self.vault_file):
            with open(self.vault_file, 'w', encoding='utf-8') as f:
                json.dump({"metadata": {"project": "Dr. Fathy Said", "version": 25.0}, "entries": {}}, f)
        
        if not os.path.exists(self.input_file):
            print(f"⚠️ [WARN] Input file {self.input_file} missing. System will wait.")

    def _get_stealth_headers(self, direct_url=None):
        """توليد هيدرز تخفي احترافية لكسر أنظمة التتبع"""
        headers = {
            "Authorization": self.auth,
            "User-Agent": self.ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Archive-Wayback-Runtime-Compatibility": "1",
            "X-Archive-Source-Stream": direct_url if direct_url else "",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }
        return headers

    @backoff.on_exception(backoff.expo, Exception, max_tries=15)
    def extract_pure_dna(self, url):
        """استخراج سرسوب البيانات الخام (الفيديو، التعليقات، الجودة)"""
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'quiet': True,
            'no_warnings': True,
            'getcomments': True,
            'cookiefile': self.cookies_file if os.path.exists(self.cookies_file) else None
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "direct_url": info.get('url'),
                "title": info.get('title'),
                "duration": info.get('duration'),
                "comments": len(info.get('comments', [])),
                "is_live": info.get('is_live', False),
                "full_data": info
            }

    @backoff.on_exception(backoff.expo, Exception, max_tries=50)
    def execute_force_archive(self, url, dna):
        """عملية الحقن القسري في Wayback Machine لضمان الخلود"""
        save_api = "https://web.archive.org/save/"
        payload = {
            "url": url,
            "capture_all": "on",            # الأزرار، التعليقات، البصمة البصرية
            "capture_outlinks": "on",       # روابط الميديا الخام
            "js_snapshot": "on",            # رندر كامل للجافا سكريبت
            "save_metadata": "on",          # الميتا-داتا السيادية
            "force_get": "on",              # تجاهل الكاش القديم
            "capture_screenshot": "on",     # لقطة شاشة 4K
            "outlinks_availability": "on"   # إجبار الأرشيف على استضافة الملفات
        }
        
        headers = self._get_stealth_headers(dna['direct_url'])
        
        # تنفيذ الهجوم
        response = self.scraper.post(save_api, data=payload, headers=headers, timeout=600)
        
        if response.status_code == 200:
            return True
        elif response.status_code == 429:
            print("\n🛑 [SHIELD ACTIVATED] Rate limit hit. Cooling down...")
            time.sleep(900) # انتظار 15 دقيقة للتبريد
            raise Exception("Rate Limit")
        return False

    def run_reactor(self):
        """تشغيل المفاعل على الروابط الموجودة في الملف"""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            links = list(dict.fromkeys([line.strip() for line in f if line.strip()]))

        print(f"🔱 TOTAL ATOMS (LINKS) TO PROCESS: {len(links)}")
        
        with tqdm(total=len(links), desc="⚛️ FUSION IN PROGRESS", colour="yellow", bar_format="{l_bar}{bar:30}{r_bar}") as pbar:
            for url in links:
                v_id = url.split("v=")[-1] if "v=" in url else url
                
                # التحقق من الخزنة
                with open(self.vault_file, 'r', encoding='utf-8') as f:
                    vault = json.load(f)
                
                if v_id in vault["entries"] and vault["entries"][v_id]["status"] == "IMMORTAL":
                    pbar.update(1)
                    continue

                try:
                    # 1. استخراج الـ DNA
                    dna = self.extract_pure_dna(url)
                    
                    # 2. حقن الأرشفة
                    success = self.execute_force_archive(url, dna)
                    
                    # 3. تسجيل النجاح
                    vault["entries"][v_id] = {
                        "status": "IMMORTAL" if success else "FAILED",
                        "title": dna["title"],
                        "duration": dna["duration"],
                        "comments_found": dna["comments"],
                        "archive_link": f"https://web.archive.org/web/*/{url}",
                        "timestamp": str(datetime.now())
                    }
                    with open(self.vault_file, 'w', encoding='utf-8') as f:
                        json.dump(vault, f, indent=4, ensure_ascii=False)
                    
                    pbar.set_postfix({"Secured": dna["title"][:20]})
                except Exception as e:
                    with open(self.error_log, 'a') as f:
                        f.write(f"{datetime.now()} - Error for {url}: {str(e)}\n")
                
                pbar.update(1)
                # زمن الاستقرار الميكانيكي (هام جداً لثبات الأرشفة)
                time.sleep(random.randint(90, 110))

if __name__ == "__main__":
    reactor = SovereignFusionReactor()
    reactor.run_reactor()
