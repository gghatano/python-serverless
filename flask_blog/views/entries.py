from flask_blog import app

@app.route('/')
def show_entries():
  # すべての記事を表示
  return "すべての記事を表示する"

@app.route('/entries', methods = ['POST'])
def add_entry():
  # 記事の作成処理を実装
  return "新しく記事が作成されました"



@app.route('/entries/new', methods = ['GET'])
def new_entry():
  # 記事の入力フォームを表示する
  return "記事の入力フォームを表示する"

@app.route('/entries/<int:id>', methods = ['GET'])
def show_entry(id):
  # 記事を取得する
  return f'記事{id}を表示'

@app.route('/entries/<int:id>/edit', methods = ['GET'])
def edit_entry(id):
  # 記事の編集フォームを表示する
  return f'記事{id}の編集フォームを表示する'

@app.route('/entries/<int:id>/update', methods = ['POST'])
def update_entry(id):
  # 記事の更新処理を実装する
  return f'記事{id}が更新されました'

@app.route('/entries/<int:id>/delete', methods = ['POST'])
def delete_entry(id):
  # 記事の削除処理を実装する
  return f'記事{id}が削除されました'

