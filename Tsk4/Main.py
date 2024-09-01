from telegram import Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler,MessageHandler,filters,CallbackQueryHandler,CallbackContext
import logging
from google_books_api_wrapper.api import GoogleBooksAPI # type: ignore
import requests
import csv

bot_token = "7038434687:AAEdz2dbZXCYvIPnNZtp1Lx5RKKPe3XztJA"
google_api = "AIzaSyDA1vLiHrzMOfgPQyCdJVLWtfK1bMtxA2w"
check_book = False
preview_book = False
Typingbook = False
Adding_book = False
Removing_book = False
temp_str =""
temp_dic = {}



#logs Errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Hello! I’m here to help you find your next great read. Just let me know what you’re interested in, and I’ll do my best to recommend some books that match your tastes. ")

async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global check_book
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Great! What genre are you interested in for your next book?")
    check_book = True

async def preview(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global preview_book
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Great! Which book would you like a preview for?")
    preview_book = True
async def plist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global Typingbook
    await context.bot.send_message(chat_id=update.effective_chat.id,text="Great! Which book would you like?")
    Typingbook = True

async def rlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Add Book", callback_data='add')],
        [InlineKeyboardButton("Remove Book", callback_data='remove')],
        [InlineKeyboardButton("Display List", callback_data='display')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)


async def _help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
Here are the available commands:

/start - Start interacting with the bot and receive a welcome message.

/book - Ask for book recommendations based on a specific genre.

/preview - Get a preview of a specific book by title.

/list - Provide the title of a book you're interested in to manage it in your reading list.

/reading_list - Manage your reading list. Options include adding, removing, and displaying books in your list.

/help - Display this help message.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)


# Callback handler for button clicks
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    action = query.data
    global Adding_book
    global Removing_book
    global temp_dic
    global temp_str
    if Adding_book:
        if context.user_data.get("r_list") == None:
            k = temp_dic[action].split("@@")
            context.user_data["r_list"] = [(k[0],k[1])]
            print("k-",k)
        else:
            k = temp_dic[action].split("@@")
            l = context.user_data.get("r_list")
            m=[]
            for i in l:
                m.append(i)
            m.append((k[0],k[1]))
            context.user_data["r_list"] = m
        Adding_book = False
        await query.edit_message_text(text="New Book Added!")
        context.user_data['action'] = None
    elif Removing_book:
        context.user_data["r_list"].pop(int(action))
        Removing_book = False
        await query.edit_message_text(text="Book Removed")


    if action == 'add':
        if temp_str == "":
            await query.edit_message_text(text="Please send the Book name to add.")
            context.user_data['action'] = 'add'
        else:
            r = Get_Book(temp_str)
            temp_str=""
            if len(r) > 1:
                await context.bot.send_message(chat_id=update.effective_chat.id,text="More than one book of same name found!")
                await context.bot.send_message(chat_id=update.effective_chat.id,text="Select your book from the list below")
                keyboard = [] 
                k = 1
                for i in r:
                    keyboard.append([InlineKeyboardButton(str(i[0]), callback_data=str(r.index(i)))])
                    temp_dic[str(r.index(i))] = str(i[0])+"@@"+str(i[1])
                    print(keyboard)
                reply_markup = InlineKeyboardMarkup(keyboard)
                await context.bot.send_message(chat_id=update.effective_chat.id,text='Choose an option:', reply_markup=reply_markup)
                Adding_book = True
                context.user_data['action'] = None
                return
            else:
                if context.user_data.get("r_list") == None:
                    context.user_data["r_list"] = [r[0],r[1]]
                else:
                    context.user_data["r_list"] = context.user_data.get("r_list").append([r[0],r[1]])
                Adding_book = False
                await context.bot.send_message(chat_id=update.effective_chat.id,text="New Book Added!")
                context.user_data['action'] = None
                return

    elif action == 'remove':
        await query.edit_message_text(text="Please select the book name to remove.")
        keyboard = [] 
        k = 1
        r = context.user_data.get("r_list")
        for i in r:
            keyboard.append([InlineKeyboardButton(str(i[0]), callback_data=str(r.index(i)))])
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(chat_id=update.effective_chat.id,text='Choose an option:', reply_markup=reply_markup)
        Removing_book = True

    
    elif action == 'display':
        l = context.user_data.get('r_list')
        f =open("Result.txt","w")
        if l == None:
            await context.bot.send_message(chat_id=update.effective_chat.id,text='No books in the reading list.\nAdd some books and try again!')
            return  
        elif len(l) == 0:
            await context.bot.send_message(chat_id=update.effective_chat.id,text='No books in the reading list.\nAdd some books and try again!')
            return
        else:
            for i in l:
                s = "Title:\n" + i[0] + "\nPreviewLink:\n"+i[1] + "\n"
                print(i)
                f.write(s)
            f.close()
            f =open("Result.txt","r")
            await query.edit_message_text(text="Here are your Results:")
            await context.bot.send_document(chat_id=update.effective_chat.id,document=f)






#Responses
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global check_book
    global preview_book
    global Adding_book
    global Typingbook
    global temp_str
    global temp_dic
    action = context.user_data.get('action')
    list = context.user_data.get('r_list')
    if action != None:
        if action == 'add':
            r = Get_Book(update.message.text)
            if len(r) == 0:
                await context.bot.send_message(chat_id=update.effective_chat.id,text="No books of that name found!")
                return
            elif len(r) > 1:
                await context.bot.send_message(chat_id=update.effective_chat.id,text="More than one book of same name found!")
                await context.bot.send_message(chat_id=update.effective_chat.id,text="Select your book from the list below")
                keyboard = [] 
                k = 1
                for i in r:
                    keyboard.append([InlineKeyboardButton(str(i[0]), callback_data=str(r.index(i)))])
                    temp_dic[str(r.index(i))] = str(i[0])+"@@"+str(i[1])
                    print(keyboard)
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text('Choose an option:', reply_markup=reply_markup)
                Adding_book = True
                context.user_data['action'] = None
                return
            else:
                if context.user_data.get("r_list") == None:
                    context.user_data["r_list"] = [r[0],r[1]]
                else:
                    context.user_data["r_list"] = context.user_data.get("r_list").append([r[0],r[1]])
                Adding_book = False
                await context.bot.send_message(chat_id=update.effective_chat.id,text="New Book Added!")
                context.user_data['action'] = None
                return
    else:
        if check_book:
            k = Get_Csv(update.message.text)
            if k == "Error":
                await context.bot.send_message(chat_id=update.effective_chat.id,text="No books of that genre found!")
                check_book = False
                return
            f =open("Books.csv","r")
            await context.bot.send_document(chat_id=update.effective_chat.id,document=f)
            check_book = False
        elif preview_book:
            r=Preview_Book(update.message.text)
            for i in r:
                s = "Title:\n"+i[0]+"\n\nAuthor(s):\n"+str(i[1])[1:-1].replace("'","")+"\n\nPreview:\n"+i[1]
                await context.bot.send_message(chat_id=update.effective_chat.id,text=s)
            else:
                if len(r) == 0:
                    await context.bot.send_message(chat_id=update.effective_chat.id,text="Sorry,But I could not find any books!. Make sure you have entered the correct title!")
            preview_book = False
        elif Typingbook:
            temp_str = update.message.text
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Great, Now use /reading_list to add or remove from your reading list!")
            Typingbook=False
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, but I didn't recognize your request!")







def Get_Csv(sub):
    try:
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=subject:"+sub)
        dic = response.json()
        books = dic["items"]
        f = open("Books.csv","w")
        writer = csv.writer(f)
        l=["title","authors","publisher","publishedDate","description","language","previewLink","infoLink"]
        writer.writerow(l)
        for j in books:
            info = j["volumeInfo"]
            result = []
            for i in l:
                try:
                    result.append(info[i])
                except:
                    result.append("Not Available")
            writer.writerow(result)
        f.close()
    except:
        return "Error"


def Get_Book(sub):
    try:
        s = sub.replace(" ","+")
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=intitle:"+s)
        dic = response.json()
        books = dic["items"]
        result = []
        for j in books:
            info = j["volumeInfo"]
            result.append([info["title"],info["previewLink"]])
        return result
    except:
        r=[]
        return r




def Preview_Book(sub):
    try:
        sub = sub.replace(" ","+")
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=intitle:"+sub)
        dic = response.json()
        books = dic["items"]
        result = []
        for j in books:
            info = j["volumeInfo"]
            print(len(books))
            try:
                result.append([info["title"],info["previewLink"]])
            except:
                result.append([info["title"],"Not Available"])
        else:
            return result
    except:
        r =[]
        return r

if __name__ == "__main__":
    application = ApplicationBuilder().token(bot_token).build()
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response)
    #Commands
    start_handler = CommandHandler('start',start)
    book_handler = CommandHandler('book',book)
    preview_handler = CommandHandler('preview',preview)
    __help = CommandHandler('help',_help)
    plist_handler = CommandHandler('list',plist)
    list_handler = CommandHandler('reading_list',rlist)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(book_handler)
    application.add_handler(message_handler)
    application.add_handler(preview_handler)
    application.add_handler(plist_handler)
    application.add_handler(list_handler)
    application.add_handler(__help)
    application.run_polling()