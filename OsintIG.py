import instaloader

def get_instagram_profile(username):
    try:
        L = instaloader.Instaloader()

        # Retrieve profile details
        profile = instaloader.Profile.from_username(L.context, username)

        # Print profile details
        print(f"Username: {profile.username}")
        print(f"Full Name: {profile.full_name}")
        print(f"Biography: {profile.biography}")
        print(f"Followers: {profile.followers}")
        print(f"Following: {profile.followees}")
        print(f"Number of Posts: {profile.mediacount}")
        
        # Print additional profile information if available
        print(f"Profile ID: {profile.userid}")
        print(f"IGTV Count: {profile.igtvcount}")

        if hasattr(profile, 'highlight_reel_count'):
            print(f"Highlight Count: {profile.highlight_reel_count}")
        else:
            print("Highlight Count: Not available")

        print(f"External URL: {profile.external_url}")
        print(f"Is Business Account: {profile.is_business_account}")
        print(f"Business Category: {profile.business_category_name}")
        

        # Print profile picture URL
        print(f"Profile Picture URL: {profile.profile_pic_url}")
        
        # Print URL to the profile on Instagram's website
        print(f"Profile URL: https://www.instagram.com/{profile.username}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile '{username}' not found.")
    except instaloader.exceptions.ConnectionException:
        print("Error: Connection error. Please check your internet connection.")

def main():
    # Get Instagram username from user input
    username = input("Enter the Instagram username to search: ")
    
    # Call function to get profile information
    get_instagram_profile(username)

if __name__ == "__main__":
    main()