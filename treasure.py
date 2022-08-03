from audioop import cross

print(
    ''',,,,,,,,,,,,,:,,:::ii;:;ii111ttftttt11i1i1t111111tt11tf1tffLCft11i1ttLLfffttt1ttt;iiii;i,i1;i:;;;;;;
::::,,,::,,::::,::;i1ti1111ttLLLfffftt1tt1tt11it1ft1tt1tttfLLtffff111tLGLLffttftti1111ii:;1:1;i;;;;;
:::::::::::::::,:;i1ttfttffffLCLLLffttttt1ttt11ftff1ft11ttffffttLCLt111tLGGLffftf11ttt1ii1t:1itii;;i
:::::::;;::::;::;;i1tffLfffffLLLLLLffttfftttfttttLftLf1ttfffffttffLCt1111LCLLfLff1ttfff11tti1it1ii;;
;;;;;;;::;;;;;;;iii1tLLLfttfffLLffLfLtffffftfftttLttLftffLftt111tffLCf1111tCLLLft1ttttf11f111it1iiii
;;;;;;;;;;;;;;;;iii1tLLLtttffLLLftLfftffffLffftttLftfLtfff1;::::;i1LCLti11ifCLLfttttttLt1ttti1ftiiii
;;;;ii;i;;;i;;;;iii1tLfftttfffLCffLLfffftfLffftttfLffLfL1::::;:::::iLCLii11itCLLLtfftfLt1tft1tft11ii
;;;;i;ii;ii;;iiiii11tffftttttfLCLfLLffffLLLLfLLfffLLfLCf:;::;;;::;;:tCCtiiiiifCCCffLffLLtfft11tt11ii
;i;iiiiiiii;iii;tt11tfLftttttfLCLLLLLLLLCLLLfLLLLLLLLLf;:;;:;;:;;;;:1Lt1iii1itCGCLLLLfLftLfttttttii1
ii;iiiiiiiiii1iifL1tffLLft1fffLLLLLLfft111iiiiiiiii11i;;;;;;;;;;;;;;iiiiiii1fCGGGCLLLLLffLttfttft111
iii;iiiiiiii11iifCtLffLLft1tttttt1111iiiiiiii;;;;;;;;;;;;;;;;;;;i;;iiiiii1tLCCGCGCCCCCLffCffftttt111
;;iiiiiiii111111LGL8GGLLfffftffftt11111111iii;;i;i;;;;;;;;;;;;iiiiiii111tC00GCGCCCCCCCCLLLffftfft111
;;i1iiiii11iit1tC0L8888GLLLLLLLLffffffffft11ii;;;;;;;;;;;;;;ii1i11i11fCG88080GCGCCCCCCCCLLLftffft111
i;;iii1111ii1tttC0L888GGCCCGGGGCCCCCCCCCLft1ii;ii;ii;;;;;;iii1tttffLLL0888800CCGCCCGCCCCCCCfffLft111
iiii111i11111tttC0C888GLCCCG0000GGGGGGCCLft1iiiiiiii;;;;i11i1tffLCCLLLCG000GCCCCGCCGCCCCCCCLfffLttt1
i1i1i11i1t11ttttL0C880CCCCCCGGGGGGGCGGGCLft1iiii;;;;ii;;iii1tLLLLLLLLCG888880LCGGCCCCCCCCCCCfLfftttt
111ii1111tttttttL0C88GCCCCCCGGGGGGGGGGGCLft11iiiiiiiiiiiii1tLCLLLLLCG08888880CCGGCCGCCGCCCCCLLLftttt
iiii1111tttttttfL0C88GCCCCCCCGGGGGGGGGGCLft111iiiii11111111tCLLLLLC08888888880GGCCCCCCGCCCCCLLLLLftt
iii111111t1ttttfLGC80CCGGCCCGGGGGGGGGGGCLftt111iii;i111111tLLLLCLC088888888800GGGCCCCCCCCCGCLLfLLfft
i1111111tttttftfLGC80GGGGCCCGGGGGGGGGGGLLftt1111i1i11111ttfCLLLCCC08888888880GGGCCCCCCGCCCGLLLLLfftt
i1111111tttttttfLGC8880GGCCCGGGGGGGGGGCLfftt11i11ii1t11tttLLLCLCCCCG8888888880CGCCCCCCGCCCCCLCLLffft
1111t11tttttffffLGG88880CCCCCCGGGGGGGGCLfttt1i1111i1t1tfffLLLLCCCCCC088888888GCGGCCGCCGCCCCCCCLLffff
1111ttttttftfffLLGG88888GCCCGGGGGGGGGCLLftttt111111ttttfLLLLLLLCCCCG0888888880CGGCCCCCCCCCCCCLLCfffL
1111ttttttftfffLCCG888880GCGGGGGGGGGCLLffttt111111t1ttfLCLLLLLCCCCCCG888888880GCCCCCCCCCCLCCCLLCLfff
1t1t1tttfftffLLLCCC888880GGGGGGGGG0GCLLftttt11111111tffLLLLLLLLCCCCCG0888888880CCCCCCCCCCLLLCLLLLLff
1111ttttfttffLLLCCC888880GGGGGGGGGGGCLfftftttt111111tffLLLLLLLLLCCCCC088888880GCCGCCCCCCCLCCCLLCLfff
11ttttttfffffLLCCCG888888GCGGGGGGG0GCLfftttttt11111ttfLLLLLLLCCCCCCGC088888880CCCGCCCCCCLLCCCLLCLtff
1ttt1tttfffffLLLCCG888880GGGGGGGGG0GCLfftttt11111ttttfLLLLLLLCCCCCCCCG88888888GCCGCCCCCCCLCCCCLCffff '''
)
print("Welcome To Treasure Island.")
print(" Your mission is to find the treasure.")
cross_road = input(
    'You\'re at a crossroad. Where do you want to go? Type "left" or "right" '
).lower()
if cross_road == "left":
    swim = input(
        'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. '
    ).lower()
    if swim == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? "
        ).lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire. Game Over")
        elif door == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over")
else:
    print("Fall into a hole. Game Over")
