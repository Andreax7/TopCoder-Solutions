
def solution(pitch, Alice, Bob):
    song=[]
    for p in pitch:
        if p not in Bob:
            song.append('Alice')
        if p not in Alice:
            song.append('Bob')
        if p in Alice and p in Bob:
            if(len(song)>0):
                posljednji = song[len(song)-1]
                song.append(posljednji)
            else:
                sljedeciInd = pitch.index(p)+1
                if pitch[sljedeciInd] in Alice and pitch[sljedeciInd] not in Bob:
                    song.append('Alice')
                if pitch[sljedeciInd] in Bob and pitch[sljedeciInd] not in Alice:
                    song.append('Bob')
                else:
                    song.append('Alice')
    print(song)
    return song

def changes(lst):
    cnt = 0
    for el in range(len(lst)-2):
        if (lst[el] == 'Bob' and lst[el+1] == 'Alice' ) or (lst[el] == 'Alice' and lst[el+1] == 'Bob') :
            cnt = cnt + 1
    print('broj izmjena ',cnt)


def main():
    pitch = [1,4,3,5,2,5,7,5,9]
   
    N = int(input("number of pitch: "))# 1-1000
    low = int(input("low pitch: ")) # 1-N
    high = int(input("high pitch: ")) # low-N

    Alice = [i for i in range(low,N+1)]  #Alice is only able to sing pitches between low and N inclusive 
    Bob = [i for i in range(1,high+1)] #Bob is only able to sing pitches between 1 and high inclusive 

    #print('Alice ', Alice,' \n Bob ', Bob)
    print(pitch, '\n')
    songs = solution(pitch, Alice, Bob)
    changes(songs)

if __name__ == "__main__":
    main()