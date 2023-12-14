import csv

dic = {
    "air":                               ["air","aria"],
    "white_wool":                        ["white wool","lana bianca"],
    "light_gray_wool":                   ["light gray_wool","lana grigio chiaro"],
    "gray_wool":                         ["gray wool","lana grigia"],
    "black_wool":                        ["black wool","lana nera"],
    "brown_wool":                        ["brown wool","lana marrone"],
    "red_wool":                          ["red wool","lana rossa"],
    "orange_wool":                       ["orange wool","lana arancione"],
    "yellow_wool":                       ["yellow wool","lana gialla"],
    "lime_wool":                         ["lime wool","lana lime"],
    "green_wool":                        ["green wool","lana verde"],
    "cyan_wool":                         ["cyan wool","lana ciano"],
    "light_blue_wool":                   ["light blue wool","lana azzurra"],
    "blue_wool":                         ["blue wool","lana blu"],
    "purple_wool":                       ["purple wool","lana viola"],
    "magenta_wool":                      ["magenta wool","lana magenta"],
    "pink_wool":                         ["pink wool","lana rosa"],
    "white_concrete":                    ["white concrete","calcestruzzo bianco"],
    "light_gray_concrete":               ["light gray concrete","calcestruzzo grigio chiaro"],
    "gray_concrete":                     ["gray concrete","calcestruzzo grigio"],
    "black_concrete":                    ["black concrete","calcestruzzo nero"],
    "brown_concrete":                    ["brown concrete","calcestruzzo marrone"],
    "red_concrete":                      ["red concrete","calcestruzzo rosso"],
    "orange_concrete":                   ["orange concrete","calcestruzzo arancione"],
    "yellow_concrete":                   ["yellow concrete","calcestruzzo giallo"],
    "lime_concrete":                     ["lime concrete","calcestruzzo lime"],
    "green_concrete":                    ["green concrete","calcestruzzo verde"],
    "cyan_concrete":                     ["cyan concrete","calcestruzzo ciano"],
    "light_blue_concrete":               ["light blue concrete","calcestruzzo azzurro"],
    "blue_concrete":                     ["blue concrete","calcestruzzo blu"],
    "purple_concrete":                   ["purple concrete","calcestruzzo viola"],
    "magenta_concrete":                  ["magenta concrete","calcestruzzo magenta"],
    "pink_concrete":                     ["pink concrete","calcestruzzo rosa"],
    "white_terracotta":                  ["white terracotta","terracotta bianca"],
    "light_gray_terracotta":             ["light gray terracotta","terracotta grigio chiaro"],
    "gray_terracotta":                   ["gray terracotta","terracotta grigia"],
    "black_terracotta":                  ["black terracotta","terracotta nera"],
    "brown_terracotta":                  ["brown terracotta","terracotta marrone"],
    "red_terracotta":                    ["red terracotta","terracotta rossa"],
    "orange_terracotta":                 ["orange terracotta","terracotta arancione"],
    "yellow_terracotta":                 ["yellow terracotta","terracotta gialla"],
    "lime_terracotta":                   ["lime terracotta","terracotta lime"],
    "green_terracotta":                  ["green terracotta","terracotta verde"],
    "cyan_terracotta":                   ["cyan terracotta","terracotta ciano"],
    "light_blue_terracotta":             ["light blue terracotta","terracotta azzurra"],
    "blue_terracotta":                   ["blue terracotta","terracotta blu"],
    "purple_terracotta":                 ["purple terracotta","terracotta viola"],
    "magenta_terracotta":                ["magenta terracotta","terracotta magenta"],
    "pink_terracotta":                   ["pink terracotta","terracotta rosa"],
    "terracotta":                        ["terracotta","terracotta"],
    "white_glazed_terracotta":           ["white glazed terracotta","terracotta smaltata bianca"],
    "light_gray_glazed_terracotta":      ["light gray glazed_terracotta","terracotta smaltata grigio chia"],
    "gray_glazed_terracotta":            ["gray glazed terracotta","terracotta smaltata grigia"],
    "black_glazed_terracotta":           ["black glazed terracotta","terracotta smaltata nera"],
    "brown_glazed_terracotta":           ["brown glazed terracotta","terracotta smaltata marrone"],
    "red_glazed_terracotta":             ["red glazed terracotta","terracotta smaltata rossa"],
    "orange_glazed_terracotta":          ["orange glazed terracotta","terracotta smaltata arancione"],
    "yellow_glazed_terracotta":          ["yellow_glazed terracotta","terracotta smaltata gialla"],
    "lime_glazed_terracotta":            ["lime glazed terracotta","terracotta smaltata lime"],
    "green_glazed_terracotta":           ["green glazed terracotta","terracotta smaltata verde"],
    "cyan_glazed_terracotta":            ["cyan glazed terracotta","terracotta smaltata ciano"],
    "light_blue_glazed_terracotta":      ["light blue glazed terracotta","terracotta smaltata azzurra"],
    "blue_glazed_terracotta":            ["blue glazed terracotta","terracotta smaltata blu"],
    "purple_glazed_terracotta":          ["purple glazed terracotta","terracotta smaltata viola"],
    "magenta_glazed_terracotta":         ["magenta glazed terracotta","terracotta smaltata magenta"],
    "pink_glazed_terracotta":            ["pink glazed terracotta","terracotta smaltata rosa"],
    "white_stained_glass":               ["white stained glass","vetro bianco"],
    "light_gray_stained_glass":          ["light gray stained_glass","vetro grigio chiaro"],
    "gray_stained_glass":                ["gray stained glass","vetro grigio"],
    "black_stained_glass":               ["black stained glass","vetro nero"],
    "brown_stained_glass":               ["brown stained glass","vetro marrone"],
    "red_stained_glass":                 ["red stained glass","vetro rosso"],
    "orange_stained_glass":              ["orange stained glass","vetro arancione"],
    "yellow_stained_glass":              ["yellow stained glass","vetro giallo"],
    "lime_stained_glass":                ["lime stained glass","vetro lime"],
    "green_stained_glass":               ["green stained glass","vetro verde"],
    "cyan_stained_glass":                ["cyan stained glass","vetro ciano"],
    "light_blue_stained_glass":          ["light blue stained glass","vetro azzurro"],
    "blue_stained_glass":                ["blue stained glass","vetro blu"],
    "purple_stained_glass":              ["purple stained glass","vetro viola"],
    "magenta_stained_glass":             ["magenta stained glass","vetro magenta"],
    "pink_stained_glass":                ["pink stained glass","vetro rosa"],
    "nether_quartz_ore":                 ["nether quartz ore","quarzo del nether"],
    "coal_ore":                          ["coal ore","minerale di carbone"],
    "iron_ore":                          ["iron ore","minerale di ferro"],
    "redstone_ore":                      ["redstone ore","minerale di redstone"],
    "lapis_ore":                         ["lapis ore","minerale di lapislazzuli"],
    "gold_ore":                          ["gold ore","minerale di oro"],
    "emerald_ore":                       ["emerald ore","minerale di smeraldo"],
    "diamond_ore":                       ["diamond ore","minerale di diamante"],
    "deepslate_coal_ore":                ["deepslate coal ore","minerale di carbone in ardesia profonda"],
    "deepslate_iron_ore":                ["deepslate iron ore","minerale di ferro in ardesia profonda"],
    "deepslate_redstone_ore":            ["deepslate redstone ore","minerale di redstone in ardesia profonda"],
    "deepslate_lapis_ore":               ["deepslate lapis ore","minerale di lapislazzuli in ardesia profonda"],
    "deepslate_gold_ore":                ["deepslate gold ore","minerale di oro in ardesia profonda"],
    "deepslate_emerald_ore":             ["deepslate emerald ore","minerale di smeraldo in ardesia profonda"],
    "deepslate_diamond_ore":             ["deepslate diamond ore","minerale di diamante in ardesia profonda"],
    "nether_bricks":                     ["nether bricks","mattoni del nether"],
    "cut_sandstone":                     ["cut sandstone","arenaria incisa"],
    "sandstone":                         ["sandstone","arenaria"],
    "mossy_cobblestone":                 ["mossy cobblestone","pietrisco muschioso"],
    "cobblestone":                       ["cobblestone","pietrisco"],
    "stone":                             ["stone","pietra"],
    "chiseled_stone_bricks":             ["chiseled stone bricks","mattoni di pietra cesellati"],
    "mossy_stone_bricks":                ["mossy stone bricks","mattoni di pietra muschiosi"],
    "stone_bricks":                      ["stone bricks","mattoni di pietra"],
    "diorite":                           ["diorite","diorite"],
    "polished_diorite":                  ["polished diorite","diorite levigata"],
    "andesite":                          ["andesite","andesite"],
    "polished_andesite":                 ["polished andesite","andesite levigata"],
    "granite":                           ["granite","granito"],
    "polished_granite":                  ["polished granite","granito levigato"],
    "dirt":                              ["dirt","terra"],
    "clay":                              ["clay","argilla"],
    "netherrack":                        ["netherrack","netherrack"],
    "prismarine_bricks":                 ["prismarine bricks","mattoni di prismarina"],
    "dark_prismarine":                   ["dark prismarine","prismarina scura"],
    "oak_wood":                          ["oak wood","legno di quercia"],
    "birch_wood":                        ["birchwood","legno di betulla"],
    "spruce_wood":                       ["spruce wood","legno di abete"],
    "dark_oak_wood":                     ["dark_oak wood","legno di quercia scura"],
    "acacia_wood":                       ["acacia wood","legno di acacia"],
    "jungle_wood":                       ["jungle wood","legno della giungla"],
    "oak_planks":                        ["oak planks","assi di quercia"],
    "birch_planks":                      ["birch planks","assi di betulla"],
    "spruce_planks":                     ["spruce planks","assi di abete"],
    "dark_oak_planks":                   ["dark_oak planks","assi di quercia scura"],
    "acacia_planks":                     ["acacia planks","assi di acacia"],
    "jungle_planks":                     ["jungle planks","assi della giungla"],
    "crimson_planks":                    ["crimson planks","assi cremisi"],
    "quartz_block":                      ["quartz block","blocco di quarzo"],
    "obsidian":                          ["obsidian","ossidiana"],
    "redstone_block":                    ["redstone block","blocco di redstone"],
    "lapis_block":                       ["lapis block","blocco di lapislazzuli"],
    "gold_block":                        ["gold block","blocco d'oro"],
    "emerald_block":                     ["emerald block","blocco di smeraldo"],
    "diamond_block":                     ["diamond block","blocco di diamante"],
    "glowstone":                         ["glowstone","luminite"],
    "jack_o_lantern":                    ["jack o' lantern","lanterna di zucca"],
    "sea_lantern":                       ["sea lantern","lanterna marina"],
    "shroomlight":                       ["shroomlight","fungolume"]
}

lanId = {
    "EN": 0,
    "IT": 1
}

of = {"IT": "di",
      "EN": "of"}
rowWord = {"IT": "Riga",
           "EN": "Row"}
required = {"IT": "Blocchi necessari",
            "EN": "Required blocks"}
total = {"IT": "Totale blocchi",
         "EN": "Total blocks"}

def read_file(path):
    posx = 0
    posy = -1
    table = [[[]]]
    mat = [[]]

    file = csv.reader(open(path, newline='', mode='r'), delimiter=',')

    for row in file:
        if posy == -1:
            width = int(row[-1])
        if posx % width == 0:
            posy += 1
            posx = 0
            if posy > 0:
                table.insert(posy,mat.copy())   # insert a matrix for each row
        table[posy].insert(posx,row)     # insert rows in each matrix
        posx += 1
    return table

def convert_to_text(table,lan):
    lanID = lanId[lan]  # array index of language
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
                    table[i][j][k] = table[i][j][k][10:]      # remove "minecraft:" from entries
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
                code[i][j] = dic.get(pixel_map[i][j])[lanID]

        code.pop(height)

        r = 0
        for row in code:
            tot = 0
            r += 1
            j = 0
            text += f"\n# {rowWord[lan]} {r}::\n"
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

                text += f"{cnt} {of[lan]} {pixel} "
                if start+1 == tot:
                    text += f"({tot})\n"
                else:
                    text += f"({start + 1} - {tot})\n"

        ingredientList.pop(0)          # row[0] is the block name, row[1] is the total
        for row in ingredientList:
            row[0] = row[0][10:]                  # remove "minecraft:"
        text += f"\n\n\n{required[lan]}:\n"
        blockTotal = 0
        for ingredient in ingredientList:
            block = dic.get(ingredient[0])[lanID]
            if block != dic.get("air")[lanID]:            # exclude air from counting
                text += f"-{block}: {ingredient[1]}\n"
                blockTotal += int(ingredient[1])
        text += f"\n{total[lan]}: {blockTotal}\n"
        return text

    except:
        return "ERROR:\nIndex out of range!"
