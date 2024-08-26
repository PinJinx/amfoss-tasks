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
Adding_book = False
temp_list=[]



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

async def rlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Add Book", callback_data='add')],
        [InlineKeyboardButton("Remove Book", callback_data='remove')],
        [InlineKeyboardButton("Display List", callback_data='display')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an option:', reply_markup=reply_markup)






# Callback handler for button clicks
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    action = query.data
    if action == 'add':
        await query.edit_message_text(text="Please send the Book name to add.")
        context.user_data['action'] = 'add'
    elif action == 'remove':
        await query.edit_message_text(text="Please send the book name to remove.")
        context.user_data['action'] = 'remove'
    elif action == 'display':
        #display
        pass



#Responses
async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global check_book
    global preview_book
    action = context.user_data.get('action')
    list = context.user_data.get('r_list')
    if action != None:
        if action == 'add':
            r = Get_Book(update.message.text)
            print(len(r))
            if len(r) > 1:
                await context.bot.send_message(chat_id=update.effective_chat.id,text="More than one book of same name found!")
                await context.bot.send_message(chat_id=update.effective_chat.id,text="Type in the Serial Number of the book from the list below")
                temp_list = []
                k = 1
                for i in r:
                    s = str(k)+")"+"Title:\n"+i[0]+"\n\nPreview:\n"+i[1]
                    await context.bot.send_message(chat_id=update.effective_chat.id,text=s)
                    temp_list.append([i[0],i[1]])
                    k+=1
                Adding_book = True
                context.user_data['action'] = None
                return
            else:
                if context.user_data.get("r_list") == None:
                    context.user_data["r_list"] = temp_list[a-1]
                else:
                    context.user_data["r_list"] = context.user_data.get("r_list").append(temp_list[a-1])
                    Adding_book = False
                await context.bot.send_message(chat_id=update.effective_chat.id,text="New Book Added!")
                context.user_data['action'] = None
                return

            


        elif action == 'remove':
            await update.message.reply_text(f'Book "{update.message.text}" removed.')
            context.user_data['action'] = None
    else:
        if check_book:
            Get_Csv(update.message.text)
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
        
        elif Adding_book:
            try:
                a = int(update.message.text)
                if a==-1:
                    Adding_book = False
                    return
                else:
                    if context.user_data.get("r_list") == None:
                        context.user_data["r_list"] = temp_list[a-1]
                    else:
                        context.user_data["r_list"] = context.user_data.get("r_list").append(temp_list[a-1])
                    Adding_book = False
                    await context.bot.send_message(chat_id=update.effective_chat.id,text="New Book Added!")
                    return
            except:
                await context.bot.send_message(chat_id=update.effective_chat.id,text="Invalid serial Number! Try Again or type -1 to return")

        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, but I didn't recognize your request!")







def Get_Csv(sub):
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


def Get_Book(sub):
    s = sub.replace(" ","+")
    response = requests.get("https://www.googleapis.com/books/v1/volumes?q=intitle:"+s)
    dic = response.json()
    books = dic["items"]
    result = []
    for j in books:
        info = j["volumeInfo"]
        result.append([info["title"],info["previewLink"]])
    return result




def Preview_Book(sub):
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

if __name__ == "__main__":
    application = ApplicationBuilder().token(bot_token).build()
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response)
    #Commands
    start_handler = CommandHandler('start',start)
    book_handler = CommandHandler('book',book)
    preview_handler = CommandHandler('preview',preview)
    list_handler = CommandHandler('reading_list',rlist)
    application.add_handler(start_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(book_handler)
    application.add_handler(message_handler)
    application.add_handler(preview_handler)
    application.add_handler(list_handler)
    application.run_polling()