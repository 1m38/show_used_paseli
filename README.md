# Show Used PASELI

KONAMIの電子マネー"PASELI"の日毎の使用額・チャージ額を集計して表示します。

## Requirements

- python3
  - beautifulsoup4
  - selenium

  ``` sh
  pip install -r requirements.txt
  ```

- Firefox
- [mozilla/gechodriver](https://github.com/mozilla/geckodriver/releases)

## Usage

1. 起動

``` sh
$ python paseli.py
```

2. 起動したFirefoxウィンドウにて、My KONAMIサイトへログイン

3. ログイン後、pythonを起動したコンソールへ戻ってEnterを押す