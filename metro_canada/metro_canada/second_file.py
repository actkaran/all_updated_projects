import random
import time
import metro_canada.db_config as db
import pymysql

from curl_cffi import requests


def status_update(id=None):
    try:
        update = f"UPDATE {db.db_link_table} SET status='saved' WHERE id=%s;"
        cur.execute(update, (id,))
        con.commit()
        print("Done...")
    except Exception as e:
        print(e)


def save_page(response=None, id=None):
    with open(f"{db.PAGESAVE}{id}.html", 'w', encoding='utf-8') as f:
        f.write(response)
        print("page saved", id)


def send_req(url):
    cookies = {
        'JSESSIONID': '524AC8AA9CA8E72C5C461FD2058C6670',
        'METRO_ANONYMOUS_COOKIE': '4e521d13-d757-43ce-b29c-089b86506922',
        'CRITEO_RETAILER_VISITOR_COOKIE': '2d1269bf-db92-43fa-9db2-85d1c254cf68',
        'APP_D_USER_ID': 'StTYrCyl-2158902408',
        'coveo_visitorId': 'ce81b714-34c2-459b-80b9-2ab8282e74df',
        'hprl': 'en',
        'NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei': '7ce2a3d962d27f5ea1cd1e3db6635daedc41859d2c02429002b6bf78a132ae009a39533e',
        '__cf_bm': 's1t0UguAASjiPzscUCeiVqice0TH_7WYD4RAUXFUibM-1730200512-1.0.1.1-paaM0V0kq7X1vESlMUs2ANuMR59r65RaEgFyKrc9AngN2Gfv7ngT7OqR_qfgtOzQ3fzCnAInGZN_NtFZV7Cj_Ht33KbPfQjFSipQS6dbwlU',
        'SameSite': 'None',
        'forterToken': '870b2a8096c9416898aef93504e9c95f_1730200521937_68_UAS9b_21ck',
        'cf_clearance': '3sE3rEGvpLKdMxZhXxmzA04fMsg1KxC.hn7osnxTIBU-1730200522-1.2.1.1-bzYPQdiZnbAgiegm.x4xOhkNVpZfRKiCVr_EiSBdrEFmWLvmlB3n4E0aGgzuPZbzEjp48joLLOCngFGpy2.k_HhUVRwAfdv8mlr42ho6SuLb83BaamiLf6WehFSeeBgxpTxzHBsZMI8Xy_d7atk0ra3.QP6Or5Ni4k59KYzVHxONlcxgxu9sK9AB8E00KzKlsnbwxnSqC.4vILT.lBRZfja9Uk5.cujB6N0ECZu5wb1xKqqMXDgZ6DZAfC5vEjZCgm4gPIlXFMlgUZwSK6wg4zPgeY1w9B5PZR6QEzjrMOPUe4HhnBb3bSn3bPVNnsQ8d2t4z2MyvDDAN5vcLRD9AK_0NwWONFL0HZ5Etn523QhrLZ4gReq32WbMyYdSvGzCggqeOyrqVoZecUmpGTvuO1ZxBquaXm1lgdw6GF3rCQ9HYterF.1eBu6UGr4U.fem',
        'forter-uid': '870b2a8096c9416898aef93504e9c95f_1730200521937_68_UAS9b_21ck_tt',
        'ADRUM_BTa': 'R:0|g:f8a86003-28a3-4e6e-b8d6-c8e75b95eadf|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11',
        'ADRUM_BT1': 'R:0|i:268164|e:377',
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-GB,en;q=0.6',
        # 'cookie': 'JSESSIONID=524AC8AA9CA8E72C5C461FD2058C6670; METRO_ANONYMOUS_COOKIE=4e521d13-d757-43ce-b29c-089b86506922; CRITEO_RETAILER_VISITOR_COOKIE=2d1269bf-db92-43fa-9db2-85d1c254cf68; APP_D_USER_ID=StTYrCyl-2158902408; coveo_visitorId=ce81b714-34c2-459b-80b9-2ab8282e74df; hprl=en; NSC_JOqrpj5ubudv2fpeodwdbrdxp2rrpei=7ce2a3d962d27f5ea1cd1e3db6635daedc41859d2c02429002b6bf78a132ae009a39533e; __cf_bm=s1t0UguAASjiPzscUCeiVqice0TH_7WYD4RAUXFUibM-1730200512-1.0.1.1-paaM0V0kq7X1vESlMUs2ANuMR59r65RaEgFyKrc9AngN2Gfv7ngT7OqR_qfgtOzQ3fzCnAInGZN_NtFZV7Cj_Ht33KbPfQjFSipQS6dbwlU; SameSite=None; forterToken=870b2a8096c9416898aef93504e9c95f_1730200521937_68_UAS9b_21ck; cf_clearance=3sE3rEGvpLKdMxZhXxmzA04fMsg1KxC.hn7osnxTIBU-1730200522-1.2.1.1-bzYPQdiZnbAgiegm.x4xOhkNVpZfRKiCVr_EiSBdrEFmWLvmlB3n4E0aGgzuPZbzEjp48joLLOCngFGpy2.k_HhUVRwAfdv8mlr42ho6SuLb83BaamiLf6WehFSeeBgxpTxzHBsZMI8Xy_d7atk0ra3.QP6Or5Ni4k59KYzVHxONlcxgxu9sK9AB8E00KzKlsnbwxnSqC.4vILT.lBRZfja9Uk5.cujB6N0ECZu5wb1xKqqMXDgZ6DZAfC5vEjZCgm4gPIlXFMlgUZwSK6wg4zPgeY1w9B5PZR6QEzjrMOPUe4HhnBb3bSn3bPVNnsQ8d2t4z2MyvDDAN5vcLRD9AK_0NwWONFL0HZ5Etn523QhrLZ4gReq32WbMyYdSvGzCggqeOyrqVoZecUmpGTvuO1ZxBquaXm1lgdw6GF3rCQ9HYterF.1eBu6UGr4U.fem; forter-uid=870b2a8096c9416898aef93504e9c95f_1730200521937_68_UAS9b_21ck_tt; ADRUM_BTa=R:0|g:f8a86003-28a3-4e6e-b8d6-c8e75b95eadf|n:metrorichelieuinc-prod_c22980fa-c09c-4712-b489-98164bef9f11; ADRUM_BT1=R:0|i:268164|e:377',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="130", "Brave";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Chromium";v="130.0.0.0", "Brave";v="130.0.0.0", "Not?A_Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
        impersonate=random.choice(["chrome110", "edge99", "safari15_5"])
    )
    return {"status": response.status_code, 'response': response.text}


if __name__ == "__main__":
    con = pymysql.connect(user=db.db_user, host=db.db_host, password=db.db_password, database=db.db_name)
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {db.db_link_table} WHERE url LIKE '%/p/%' AND status='pending' LIMIT 1000;")
    data = cur.fetchall()
    for i in data:
        url = i[1]
        id = i[0]
        temp_var = send_req(url=url)
        if temp_var["status"] == 200:
            save_page(temp_var["response"], id)
            status_update(id)
            tim = random.choice([3.12, 2.76])
            time.sleep(tim)
        else:
            print(temp_var["status"])
