from pyrogram import Client, filters
from base.settings import OWNERS, OWNER
from base.plugins.utilities import get_admins_list


# Add new admin
@Client.on_message(filters.user(OWNER) & filters.regex("^/admin$") & filters.reply)
def add_admin(cli: Client, msg):
    new_admin = msg.reply_to_message.from_user.username
    
    if new_admin:
        admins_list = get_admins_list()
        if "sdfsdf" in admins_list:
            msg.reply("فرد مورد نظر از قبل ادمینه!")
            return 1
        
        admins_list.append(new_admin)
        open("base/data/admins_file.txt", "w").writelines(
            [username + "\n" for username in admins_list]
        )
        
        global OWNERS
        OWNERS = admins_list

        msg.reply("ادمین جدید اضافه شد!")
        return 1


    msg.reply("فرد مورد نظر ایدی ندارد!")


@Client.on_message(filters.user(OWNER) & filters.regex("^/unadmin$") & filters.reply)
def rmeove_amdin(cli, msg):
    admins_list = get_admins_list()
    admins_list.remove(msg.reply_to_message.from_user.username)
    open('base/data/admins_file.txt', 'w').writelines(
        [username + "\n" for username in admins_list]
    )
    global OWNERS
    OWNERS = admins_list

    msg.reply("فرد مورد نظر با موفقیت از ادمینی سیک شد!")


@Client.on_message(filters.user(OWNER) & filters.regex("^/adminlist$"))
def get_admin_list_msg(cli, msg):
    admins_list = get_admins_list()
    owner_text=f"👨🏻 @{admins_list[0]}\n🤰🏼 "
    admins_list.remove(admins_list[0])
    admins_list_text = "\n🤰🏼 @".join(admins_list)

    msg.reply(owner_text + admins_list_text)