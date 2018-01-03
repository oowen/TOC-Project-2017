# Love bot

## prerequirement
 - python3
 - telegram
 - network
 - ngrok

## setup
    pip3 install requirement.txt

## purpose
1.教不到女友,寫個機器人騙騙自己。

## usage
讓每天多一點色彩,但千萬不能想起他只是個機器人,不然生活會更黑白.

## STATE<br>
### init
1. user state:
 - 	input '晚安'		go to state1
 - 	input '我想你了'	go to state2
 - 	input 'love you'	go to state3
 - 	input '我很難過'	go to state4
 - 	input '我生病了'	go to state5
 - 	input '今天天氣真好'	go to state6
 - 	input '<3'		go to state7
 - 	input '你在生氣嗎'	go to state8
 - 	input '寶貝在嗎'	go to state9
 - 	input '你在哪裡呢'	go to state10
### 關心
1. state9:
	寶貝回應 '我一直都在'
	back to user state
2. state8:
	寶貝回應 '我只是覺得我們可以更好,不是嗎:('
	back to user state
3. state10:
        寶貝回應 '我在捷運站,想我了嗎哈哈哈~~'
	back to user state
### 需要人陪
1. state2:
        寶貝回應 '我也很想你ㄚ QQ..'
	back to user state
2. state4:
        寶貝回應 '寶貝,我沒辦法時時刻刻再你身邊,你要好好照顧自己，我愛你'
	back to user state
3. state5:
        寶貝回應 '你的健康是我最大的幸福，讓我一直陪伴你吧'
	back to user state
4. state6:
        寶貝回應 '那我們快去約會！！'
	back to user state
### 只想說說話
1. state1:
        寶貝回應 '晚安,親愛的:)'
	back to user state
2. state3:
        寶貝回應 'me too ^o^'
	back to user state
3. state7:
        寶貝回應 '<333'
	back to user state
## problem
1. 傳送的詞語必須明確
2. 寶貝只會說這幾句話,很快就膩了
## next objective
1. 寶貝會傳自拍照 
2. 對話更人性化
