import requests
from data import cdn , bearer_token
# آدرس API





post_id = 11242  # شناسه پست مورد نظر


response = requests.post(f"https://www.vod.tarinet.ir.cartoonflix.ir/wp-json/wp/v2/posts/{post_id}", headers={ "Authorization": f"Bearer {bearer_token}", "Content-Type": "application/json" }, json={ "categories" : [7558] })

if response.status_code == 200:
    print("cat Post updated successfully")
else:
    print("Failed to update post:", response.text)
