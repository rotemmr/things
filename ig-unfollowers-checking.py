import json

def extract_handles(data):
    handles = []
    for item in data:
        if 'string_list_data' in item:
            for entry in item['string_list_data']:
                handles.append(entry['value'])
    return set(handles)

def main():
    with open('following.json', 'r') as f:
        following_data = json.load(f)
    with open('followers.json', 'r') as f:
        followers_data = json.load(f)

    following_handles = extract_handles(following_data['relationships_following'])
    followers_handles = extract_handles(followers_data)
    
    
    non_followers = following_handles - followers_handles
    
    
    with open('non_followers.txt', 'w') as f:
        
        f.write(f"Number of users you are following who aren't following you back: {len(non_followers)}\n\n")
        
        
        for i, handle in enumerate(non_followers, start=1):
            f.write(f"{i}. {handle}\n")

    

if _name_ == "_main_":
    main()
