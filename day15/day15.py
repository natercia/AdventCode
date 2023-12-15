def hash(st):
    cValue = 0
    stList = [*st]
    for s in stList:
        cValue = ((cValue + ord(s)) * 17) % 256
    return cValue
    
def hashMap(inputList):
    boxes = [{} for _ in range(256)]
    for i in inputList:
      if '-' in i:
        toRemove = i.replace("-", "")
        if toRemove in boxes[hash(toRemove)]:
          del boxes[hash(toRemove)][toRemove]
      if '=' in i:
        splitted = i.split("=")
        boxes[hash(splitted[0])][splitted[0]] = int(splitted[1])
    return boxes

def main():
    f = open("input.txt", "r")
    inputList = (f.read()).strip().split(",")
    boxes = hashMap(inputList)
    count = 0
    sumCValue = 0
    for box in boxes:
      count2 = 1
      for key in box:
        sumCValue = sumCValue + ((1 + count) * count2 * box[key])
        count2 = count2 + 1
      count = count + 1
    print("FINAL SUM:"+ str(sumCValue))

if __name__ == "__main__":
    main()