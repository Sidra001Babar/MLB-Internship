def calculateStatistics(results):

    totalSpaces = 0
    emptySpaces = 0
    occupiedSpaces = 0


    boxes = results[0].boxes


    for box in boxes:

        classId = int(box.cls[0])

        totalSpaces += 1


        if classId == 0:
            emptySpaces += 1

        else:
            occupiedSpaces += 1



    if totalSpaces > 0:
        occupancyPercentage = (
            occupiedSpaces / totalSpaces
        ) * 100

    else:
        occupancyPercentage = 0



    statistics = {

        "Total Spaces": totalSpaces,

        "Empty Spaces": emptySpaces,

        "Occupied Spaces": occupiedSpaces,

        "Occupancy Percentage": round(
            occupancyPercentage,
            2
        )

    }


    return statistics