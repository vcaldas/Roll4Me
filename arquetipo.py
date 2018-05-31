arquetipos = {
    'Arquiteto': 'Você constrói algo de valor duradouro',
    'Autocrata': 'Você precisa de controle.',
    'Bon Vivant': 'A não-vida é para o prazer.',
    'Caçador de Emoções': 'A corrida é o que importa',
    'Camaleão': 'Você consegue se misturar em qualquer situação.',
    'Capitalista': ' Por que entregar de graça quando você pode vender?',
    'Celebrante': ' A sua causa lhe traz alegria',
    'Cientista': ' Tudo é um enigma para ser resolvido',
    'Criança': ' Será que alguém não esta lá por você?',
    'Conpetidor': ' Você deve ser o melhor.',
    'Conformista': ' Você segue e assiste',
    'Diletante': ' É sempre sobre a próxima grande coisa',
    'Diretor': ' Você supervisiona o que deve ser feito',
    'Enigma': ' Apenas quando as pessoas pensam que você figurou algo, você muda o jogo',
    'Esperto': ' Existem outros para seu benefício.',
    'Excêntrico': ' O status quo é para os ovinos',
    'Fanático': ' A causa é tudo que importa',
    'Galante': ' Você não é a canção mais aplaudida: você é o show!',
    'Guru': ' Pessoas o acham espiritualmente convincente.',
    'Idealista': ' Você acredita em algo maior.',
    'Juiz': ' Seu julgamento irá melhorar as coisas',
    'Malandro': ' Rir ofusca a dor.',
    'Mártir': ' Você sofre para o bem maior.',
    'Masoquista': ' A dor lembra que você ainda existe',
    'Monstro': ' Você é Amaldiçoado, assim, aja como tal!',
    'Olho da Tempestade': ' Caos e destruição o seguem, mas nunca chegam a você.',
    'Pedagogo': ' Você salva outros através do conhecimento.',
    'Penitente': ' A não-vida é uma maldição, e você deve expiar por isso',
    'Perfeccionista': ' Se esforça para a meta inatingível',
    'Ranzinza': ' Tudo tem suas falhas',
    'Rebelde': ' Você não segue as regras de ninguém.',
    'Ladino': ' É tudo sobre você.',
    'Sadista': ' Você vive para causar dor.',
    'Samaritano': ' Todos precisam de carinho',
    'Show de Horrores': ' Alvos repugnantes o faz sorrir.',
    'Sociopata': ' O inferior deve ser destruído.',
    'Solitário': ' Você faz seu próprio',
    'Soldado': ' Você segue ordens, mas da sua própria maneira.',
    'Sobrevivente': ' Nada pode te manter no chão.',
    'Tradicionalista': ' Como sempre foi, por isso deve ser.',
    'Valentão': ' O poder dá razão.',
    'Visionário': ' Algo existe além de tudo isso', }


def format_print(key, value):
    string = ("|Arquetipo| " + key + " : " + value)
    return string


def check_key(query):
    flag = False
    my_key = ""
    my_value = ""

    for key, value in arquetipos.items():
        if query.upper() in key.upper():
            flag = True
            my_key = key
            my_value = value

    return flag, my_key, my_value


def get_info(query):
    flag, key, value = check_key(query)

    if flag:
        return format_print(key, value)
    else:
        return "Arquetipo : " + query + "| não encontrado."

