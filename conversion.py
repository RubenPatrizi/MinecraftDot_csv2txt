import csv

dic = {
    "air":"A",
    "white_wool":"B",
    "light_gray_wool":"C",
    "gray_wool":"D",
    "black_wool":"E",
    "brown_wool":"F",
    "red_wool":"G",
    "orange_wool":"H",
    "yellow_wool":"I",
    "lime_wool":"J",
    "green_wool":"K",
    "cyan_wool":"L",
    "light_blue_wool":"M",
    "blue_wool":"N",
    "purple_wool":"O",
    "magenta_wool":"P",
    "pink_wool":"Q",
    "white_concrete":"R",
    "light_gray_concrete":"S",
    "gray_concrete":"T",
    "black_concrete":"U",
    "brown_concrete":"V",
    "red_concrete":"W",
    "orange_concrete":"X",
    "yellow_concrete":"Y",
    "lime_concrete":"Z",
    "green_concrete":"A1",
    "cyan_concrete":"B1",
    "light_blue_concrete":"C1",
    "blue_concrete":"D1",
    "purple_concrete":"E1",
    "magenta_concrete":"F1",
    "pink_concrete":"G1",
    "white_terracotta":"H1",
    "light_gray_terracotta":"I1",
    "gray_terracotta":"J1",
    "black_terracotta":"K1",
    "brown_terracotta":"L1",
    "red_terracotta":"M1",
    "orange_terracotta":"N1",
    "yellow_terracotta":"O1",
    "lime_terracotta":"P1",
    "green_terracotta":"Q1",
    "cyan_terracotta":"R1",
    "light_blue_terracotta":"S1",
    "blue_terracotta":"T1",
    "purple_terracotta":"U1",
    "magenta_terracotta":"V1",
    "pink_terracotta":"W1",
    "terracotta":"X1",
    "white_glazed_terracotta":"Y1",
    "light_gray_glazed_terracotta":"Z1",
    "gray_glazed_terracotta":"A2",
    "black_glazed_terracotta":"B2",
    "brown_glazed_terracotta":"C2",
    "red_glazed_terracotta":"D2",
    "orange_glazed_terracotta":"E2",
    "yellow_glazed_terracotta":"F2",
    "lime_glazed_terracotta":"G2",
    "green_glazed_terracotta":"H2",
    "cyan_glazed_terracotta":"I2",
    "light_blue_glazed_terracotta":"J2",
    "blue_glazed_terracotta":"K2",
    "purple_glazed_terracotta":"L2",
    "magenta_glazed_terracotta":"M2",
    "pink_glazed_terracotta":"N2",
    "white_stained_glass":"O2",
    "light_gray_stained_glass":"P2",
    "gray_stained_glass":"Q2",
    "black_stained_glass":"R2",
    "brown_stained_glass":"S2",
    "red_stained_glass":"T2",
    "orange_stained_glass":"U2",
    "yellow_stained_glass":"V2",
    "lime_stained_glass":"W2",
    "green_stained_glass":"X2",
    "cyan_stained_glass":"Y2",
    "light_blue_stained_glass":"Z2",
    "blue_stained_glass":"A3",
    "purple_stained_glass":"B3",
    "magenta_stained_glass":"C3",
    "pink_stained_glass":"D3",
    "nether_quartz_ore":"E3",
    "coal_ore":"F3",
    "iron_ore":"G3",
    "redstone_ore":"H3",
    "lapis_ore":"I3",
    "gold_ore":"J3",
    "emerald_ore":"K3",
    "diamond_ore":"L3",
    "deepslate_coal_ore":"M3",
    "deepslate_iron_ore":"N3",
    "deepslate_redstone_ore":"O3",
    "deepslate_lapis_ore":"P3",
    "deepslate_gold_ore":"Q3",
    "deepslate_emerald_ore":"R3",
    "deepslate_diamond_ore":"S3",
    "nether_bricks":"T3",
    "cut_sandstone":"U3",
    "sandstone":"V3",
    "mossy_cobblestone":"W3",
    "cobblestone":"X3",
    "stone":"Y3",
    "chiseled_stone_bricks":"Z3",
    "mossy_stone_bricks":"A4",
    "stone_bricks":"B4",
    "diorite":"C4",
    "polished_diorite":"D4",
    "andesite":"E4",
    "polished_andesite":"F4",
    "granite":"G4",
    "polished_granite":"H4",
    "dirt":"I4",
    "clay":"J4",
    "netherrack":"K4",
    "prismarine_bricks":"L4",
    "dark_prismarine":"M4",
    "oak_wood":"N4",
    "birch_wood":"O4",
    "spruce_wood":"P4",
    "dark_oak_wood":"Q4",
    "acacia_wood":"R4",
    "jungle_wood":"S4",
    "oak_planks":"T4",
    "birch_planks":"U4",
    "spruce_planks":"V4",
    "dark_oak_planks":"W4",
    "acacia_planks":"X4",
    "jungle_planks":"Y4",
    "crimson_planks":"Z4",
    "quartz_block":"A5",
    "obsidian":"B5",
    "redstone_block":"C5",
    "lapis_block":"D5",
    "gold_block":"E5",
    "emerald_block":"F5",
    "diamond_block":"G5",
    "glowstone":"H5",
    "jack_o_lantern":"I5",
    "sea_lantern":"J5",
    "shroomlight":"K5",
}

cid_en = {
    "A":"air",
    "B":"white wool",
    "C":"light gray_wool",
    "D":"gray wool",
    "E":"black wool",
    "F":"brown wool",
    "G":"red wool",
    "H":"orange wool",
    "I":"yellow wool",
    "J":"lime wool",
    "K":"green wool",
    "L":"cyan wool",
    "M":"light blue wool",
    "N":"blue wool",
    "O":"purple wool",
    "P":"magenta wool",
    "Q":"pink wool",
    "R":"white concrete",
    "S":"light gray concrete",
    "T":"gray concrete",
    "U":"black concrete",
    "V":"brown concrete",
    "W":"red concrete",
    "X":"orange concrete",
    "Y":"yellow concrete",
    "Z":"lime concrete",
    "A1":"green concrete",
    "B1":"cyan concrete",
    "C1":"light blue concrete",
    "D1":"blue concrete",
    "E1":"purple concrete",
    "F1":"magenta concrete",
    "G1":"pink concrete",
    "H1":"white terracotta",
    "I1":"light gray terracotta",
    "J1":"gray terracotta",
    "K1":"black terracotta",
    "L1":"brown terracotta",
    "M1":"red terracotta",
    "N1":"orange terracotta",
    "O1":"yellow terracotta",
    "P1":"lime terracotta",
    "Q1":"green terracotta",
    "R1":"cyan terracotta",
    "S1":"light blue terracotta",
    "T1":"blue terracotta",
    "U1":"purple terracotta",
    "V1":"magenta terracotta",
    "W1":"pink terracotta",
    "X1":"terracotta",
    "Y1":"white glazed terracotta",
    "Z1":"light gray glazed_terracotta",
    "A2":"gray glazed terracotta",
    "B2":"black glazed terracotta",
    "C2":"brown glazed terracotta",
    "D2":"red glazed terracotta",
    "E2":"orange glazed terracotta",
    "F2":"yellow_glazed terracotta",
    "G2":"lime glazed terracotta",
    "H2":"green glazed terracotta",
    "I2":"cyan glazed terracotta",
    "J2":"light blue glazed terracotta",
    "K2":"blue glazed terracotta",
    "L2":"purple glazed terracotta",
    "M2":"magenta glazed terracotta",
    "N2":"pink glazed terracotta",
    "O2":"white stained glass",
    "P2":"light gray stained_glass",
    "Q2":"gray stained glass",
    "R2":"black stained glass",
    "S2":"brown stained glass",
    "T2":"red stained glass",
    "U2":"orange stained glass",
    "V2":"yellow stained glass",
    "W2":"lime stained glass",
    "X2":"green stained glass",
    "Y2":"cyan stained glass",
    "Z2":"light blue stained glass",
    "A3":"blue stained glass",
    "B3":"purple stained glass",
    "C3":"magenta stained glass",
    "D3":"pink stained glass",
    "E3":"nether quartz ore",
    "F3":"coal ore",
    "G3":"iron ore",
    "H3":"redstone ore",
    "I3":"lapis ore",
    "J3":"gold ore",
    "K3":"emerald ore",
    "L3":"diamond ore",
    "M3":"deepslate coal ore",
    "N3":"deepslate iron ore",
    "O3":"deepslate redstone ore",
    "P3":"deepslate lapis ore",
    "Q3":"deepslate gold ore",
    "R3":"deepslate emerald ore",
    "S3":"deepslate diamond ore",
    "T3":"nether bricks",
    "U3":"cut sandstone",
    "V3":"sandstone",
    "W3":"mossy cobblestone",
    "X3":"cobblestone",
    "Y3":"stone",
    "Z3":"chiseled stone bricks",
    "A4":"mossy stone bricks",
    "B4":"stone bricks",
    "C4":"diorite",
    "D4":"polished diorite",
    "E4":"andesite",
    "F4":"polished andesite",
    "G4":"granite",
    "H4":"polished granite",
    "I4":"dirt",
    "J4":"clay",
    "K4":"netherrack",
    "L4":"prismarine bricks",
    "M4":"dark prismarine",
    "N4":"oak wood",
    "O4":"birchwood",
    "P4":"spruce wood",
    "Q4":"dark_oak wood",
    "R4":"acacia wood",
    "S4":"jungle wood",
    "T4":"oak planks",
    "U4":"birch planks",
    "V4":"spruce planks",
    "W4":"dark_oak planks",
    "X4":"acacia planks",
    "Y4":"jungle planks",
    "Z4":"crimson planks",
    "A5":"quartz block",
    "B5":"obsidian",
    "C5":"redstone block",
    "D5":"lapis block",
    "E5":"gold block",
    "F5":"emerald block",
    "G5":"diamond block",
    "H5":"glowstone",
    "I5":"jack o' lantern",
    "J5":"sea lantern",
    "K5":"shroomlight",
}

cid_it = {
    "A":"aria",
    "B":"lana bianca",
    "C":"lana grigio chiaro",
    "D":"lana grigia",
    "E":"lana nera",
    "F":"lana marrone",
    "G":"lana rossa",
    "H":"lana arancione",
    "I":"lana gialla",
    "J":"lana lime",
    "K":"lana verde",
    "L":"lana ciano",
    "M":"lana azzurra",
    "N":"lana blu",
    "O":"lana viola",
    "P":"lana magenta",
    "Q":"lana rosa",
    "R":"calcestruzzo bianco",
    "S":"calcestruzzo grigio chiaro",
    "T":"calcestruzzo grigio",
    "U":"calcestruzzo nero",
    "V":"calcestruzzo marrone",
    "W":"calcestruzzo rosso",
    "X":"calcestruzzo arancione",
    "Y":"calcestruzzo giallo",
    "Z":"calcestruzzo lime",
    "A1":"calcestruzzo verde",
    "B1":"calcestruzzo ciano",
    "C1":"calcestruzzo azzurro",
    "D1":"calcestruzzo blu",
    "E1":"calcestruzzo viola",
    "F1":"calcestruzzo magenta",
    "G1":"calcestruzzo rosa",
    "H1":"terracotta bianca",
    "I1":"terracotta grigio chiaro",
    "J1":"terracotta grigia",
    "K1":"terracotta nera",
    "L1":"terracotta marrone",
    "M1":"terracotta rossa",
    "N1":"terracotta arancione",
    "O1":"terracotta gialla",
    "P1":"terracotta lime",
    "Q1":"terracotta verde",
    "R1":"terracotta ciano",
    "S1":"terracotta azzurra",
    "T1":"terracotta blu",
    "U1":"terracotta viola",
    "V1":"terracotta magenta",
    "W1":"terracotta rosa",
    "X1":"terracotta",
    "Y1":"terracotta smaltata bianca",
    "Z1":"terracotta smaltata grigio chia",
    "A2":"terracotta smaltata grigia",
    "B2":"terracotta smaltata nera",
    "C2":"terracotta smaltata marrone",
    "D2":"terracotta smaltata rossa",
    "E2":"terracotta smaltata arancione",
    "F2":"terracotta smaltata gialla",
    "G2":"terracotta smaltata lime",
    "H2":"terracotta smaltata verde",
    "I2":"terracotta smaltata ciano",
    "J2":"terracotta smaltata azzurra",
    "K2":"terracotta smaltata blu",
    "L2":"terracotta smaltata viola",
    "M2":"terracotta smaltata magenta",
    "N2":"terracotta smaltata rosa",
    "O2":"vetro bianco",
    "P2":"vetro grigio chiaro",
    "Q2":"vetro grigio",
    "R2":"vetro nero",
    "S2":"vetro marrone",
    "T2":"vetro rosso",
    "U2":"vetro arancione",
    "V2":"vetro giallo",
    "W2":"vetro lime",
    "X2":"vetro verde",
    "Y2":"vetro ciano",
    "Z2":"vetro azzurro",
    "A3":"vetro blu",
    "B3":"vetro viola",
    "C3":"vetro magenta",
    "D3":"vetro rosa",
    "E3":"quarzo del nether",
    "F3":"minerale di carbone",
    "G3":"minerale di ferro",
    "H3":"minerale di redstone",
    "I3":"minerale di lapislazzuli",
    "J3":"minerale di oro",
    "K3":"minerale di smeraldo",
    "L3":"minerale di diamante",
    "M3":"minerale di carbone in ardesia profonda",
    "N3":"minerale di ferro in ardesia profonda",
    "O3":"minerale di redstone in ardesia profonda",
    "P3":"minerale di lapislazzuli in ardesia profonda",
    "Q3":"minerale di oro in ardesia profonda",
    "R3":"minerale di smeraldo in ardesia profonda",
    "S3":"minerale di diamante in ardesia profonda",
    "T3":"mattoni del nether",
    "U3":"arenaria incisa",
    "V3":"arenaria",
    "W3":"pietrisco muschioso",
    "X3":"pietrisco",
    "Y3":"pietra",
    "Z3":"mattoni di pietra cesellati",
    "A4":"mattoni di pietra muschiosi",
    "B4":"mattoni di pietra",
    "C4":"diorite",
    "D4":"diorite levigata",
    "E4":"andesite",
    "F4":"andesite levigata",
    "G4":"granito",
    "H4":"granito levigato",
    "I4":"terra",
    "J4":"argilla",
    "K4":"netherrack",
    "L4":"mattoni di prismarina",
    "M4":"prismarina scura",
    "N4":"legno di quercia",
    "O4":"legno di betulla",
    "P4":"legno di abete",
    "Q4":"legno di quercia scura",
    "R4":"legno di acacia",
    "S4":"legno della giungla",
    "T4":"assi di quercia",
    "U4":"assi di betulla",
    "V4":"assi di abete",
    "W4":"assi di quercia scura",
    "X4":"assi di acacia",
    "Y4":"assi della giungla",
    "Z4":"assi cremisi",
    "A5":"blocco di quarzo",
    "B5":"ossidiana",
    "C5":"blocco di redstone",
    "D5":"blocco di lapislazzuli",
    "E5":"blocco d'oro",
    "F5":"blocco di smeraldo",
    "G5":"blocco di diamante",
    "H5":"luminite",
    "I5":"lanterna di zucca",
    "J5":"lanterna marina",
    "K5":"fungolume"
}

def read_file(path):
    n1 = 0
    n2 = -1
    x = [[[]]]
    y = [[]]

    file = csv.reader(open(path, newline='', mode='r'), delimiter=',')

    for i in file:
        if n2 == -1:
            width = int(i[-1])
        if n1 % width == 0:
            n2 += 1
            n1 = 0
            if n2 > 0:
                x.insert(n2,y.copy())
        x[n2].insert(n1,i)
        n1 += 1
    return x

def convert_to_text(table,lan):
    try:
        text = ""
        width = int(table[0][0][-1])
        table[0].pop(0)
        table[-1].pop(-1)
        end = 0
        height = 0

        i = 0
        while i < len(table):
            j = 0
            while j < len(table[i]):
                k = 0
                if len(table[i][j]) == 0:
                    if i == len(table) - 1:
                        end = j
                    table[i].pop(j)
                    break
                while k < len(table[i][j]):
                    table[i][j][k] = table[i][j][k][10:]
                    k += 1
                if end != 0:
                    break
                height += 1
                j += 1
            if end != 0:
                break
            i += 1

        code = [[]]
        for i in range(0, height):
            code.append([])
            for j in range(0, width):
                code[i].append(0)

        for section in table:
            for row in section:
                row.pop(0)

        ingredientList = table[len(table)-1][end:]
        table[len(table)-1] = table[len(table)-1][:end]
        for section in table[1:]:
            for row in section:
                table[0].append(row)

        pixel_map = table.pop(0)

        for i in range(0,height):
            for j in range(0,width):
                code[i][j] = dic.get(pixel_map[i][j])

        code.pop(height)

        r = 0
        for row in code:
            tot = 0
            r += 1
            j = 0
            if lan == "IT":
                text += f"\nRiga {r}::\n"
            if lan == "EN":
                text += f"\nRow {r}::\n"
            for i in range(0,width):
                if j == width:
                    break
                i = j
                cnt = 0
                start = i
                pixel = row[i]
                j = i
                while pixel == row[j] and j < width:
                    cnt += 1
                    j += 1
                    tot += 1
                    if j == width:
                        break
                i = j
                if start+1 == tot:
                    if lan == "IT":
                        text += f"{cnt} di {cid_it.get(pixel)}  ({tot})\n"
                    if lan == "EN":
                        text += f"{cnt} of {cid_en.get(pixel)}  ({tot})\n"
                else:
                    if lan == "IT":
                        text += f"{cnt} di {cid_it.get(pixel)}  ({start + 1} - {tot})\n"
                    if lan == "EN":
                        text += f"{cnt} of {cid_en.get(pixel)}  ({start + 1} - {tot})\n"

        ingredientList.pop(0)
        for row in ingredientList:
            row[0] = row[0][10:]
        if lan == "IT":
            text += "\n\n\nBlocchi necessari:\n"
        if lan == "EN":
            text += "\n\n\nRequired blocks:\n"
        blockTotal = 0
        for ingredient in ingredientList:
            blockCode = dic.get(ingredient[0])
            if blockCode != "A":
                if lan == "IT":
                    text += f"{cid_it.get(blockCode)}: {ingredient[1]}\n"
                if lan == "EN":
                    text += f"{cid_en.get(blockCode)}: {ingredient[1]}\n"
                blockTotal += int(ingredient[1])
        if lan == "IT":
            text += f"\nTotale blocchi: {blockTotal}\n"
        if lan == "EN":
            text += f"\nTotal blocks: {blockTotal}\n"
        return text

    except:
        return "ERROR:\nIndex out of range!"
