import streamlit as st
import random

versiculos_lista = [('1','Tomai também o capacete da salvação, e a espada do Espírito, que é a palavra de Deus; Efésios 6:17'),
                    ('2','...com o coração se crê para a justiça, e com a boca se faz confissão para a salvação ... Romanos 10:10'),
                    ('3',' ...toda a carne verá a salvação de Deus. Lucas 3:6'),
                    ('4','Mas devemos sempre dar graças a Deus por vós, irmãos amados do SENHOR, por vos ter Deus elegido desde o princípio para a salvação, em santificação do Espírito, e fé da verdade; II Tessalonicenses 2:13'),
                    ('5', 'E, sendo Ele consumado, veio a ser a causa da eterna salvação para todos os que Lhe obedecem; Hebreus 5:9'),
                    ('6', '... não me envergonho do evangelho de Cristo, pois é o poder de Deus para salvação de todo aquele que crê; ... Romanos 1:16'),
                    ('7', '... se somos atribulados, é para vossa consolação e salvação; ou, se somos consolados, para vossa consolação e salvação é,a qual se opera suportando com paciência as mesmas aflições que nós também padecemos; II Coríntios 1:6'),
                    ('8', '... Deus não nos destinou para a ira, mas para a aquisição da salvação, por nosso Senhor Jesus Cristo, I Tessalonicenses 5:9'),
                    ('9', '... a graça de Deus se há manifestado, trazendo salvação a todos os homens, Tito 2:11'),
                    ('10', 'Que mediante a fé estais guardados na virtude de Deus para a salvação, já prestes para se revelar no último tempo, I Pedro 1:5'),
                    ('11', 'SENHOR, guia-me na Tua justiça, por causa dos meus inimigos; endireita diante de mim o Teu caminho.Salmos 5:8'),
                    ('12', 'Guia-me na Tua verdade, e ensina-me, pois Tu és o Deus da minha salvação; por Ti estou esperando todo o dia.Salmos 25:5'),
                    ('13', 'Porque Tu és a minha rocha e a minha fortaleza; assim, por amor do Teu nome, guia-me e encaminha-me. Salmos 31:3'),
                    ('14', 'Guiar-me-ás com o Teu conselho, e depois me receberás na glória. Salmos 73:24'),
                    ('15', 'E guiarei os cegos pelo caminho que nunca conheceram, fá-los-ei caminhar pelas veredas que não conheceram; tornarei as trevas em luz perante eles, e as coisas tortas farei direitas. Estas coisas lhes farei, e nunca os desampararei. Isaías 42:16'),
                    ('17', 'Deitar-me faz em verdes pastos, guia-me mansamente a águas tranquilas. Salmos 23:2'),
                    ('18', 'Guiará os mansos em justiça e aos mansos ensinará o Seu caminho. Salmos 25.9'),
                    ('19', 'Instruir-te-ei, e ensinar-te-ei o caminho que deves seguir; guiar-te-ei com os Meus olhos. Salmos 32:8'),
                    ('20', 'Até ali a Tua mão me guiará e a Tua destra me susterá. Salmos 139:10'),
                    ('21', 'Assim diz o SENHOR, o teu Redentor, o Santo de Israel: Eu sou o SENHOR teu Deus, que te ensina o que é útil, e te guia pelo caminho em que deves andar. Isaías 48:17'),
                    ('22', 'Refrigera a minha alma; guia-me pelas veredas da justiça, por amor do Seu nome. Salmos 23:3'),
                    ('23', 'Ensina-me,SENHOR, o Teu caminho, e guia-me pela vereda direita ... Salmos 27:11'),
                    ('24', 'Porque este Deus é o nosso Deus para sempre; Ele será nosso guia até à morte.Salmos 48:14'),
                    ('25', 'E vê se há em mim algum caminho mau, e guia-me pelo caminho eterno. Salmos 139:24'),
                    ('26', 'Porque o Cordeiro que está no meio do trono os apascentará, e lhes servirá de guia para as fontes das águas da vida; e Deus limpará de seus olhos toda a lágrima. Apocalipse 7:17'),
                    ('27', 'Louvai ao SENHOR, invocai o Seu nome, fazei conhecidas as Suas obras entre os povos. I Crônicas 16:8'),
                    ('28', 'Louvai ao SENHOR, porque é bom: pois a Sua benignidade dura perpetuamente. I Crônicas 16:34'),
                    ('29', 'EU Te louvarei, SENHOR, com todo o meu coração; contarei todas as Tuas maravilhas. Salmos 9:1'),
                    ('30', 'O SENHOR é a minha força e o meu escudo; nEle confiou o meu coração, e fui socorrido; assim o meu coração salta de prazer, e com o meu canto O louvarei. Salmos 28:7'),
                    ('31', 'E assim a minha língua falará da Tua justiça e do Teu louvor todo o dia. Salmos 35:28'),
                    ('32', 'Porque grande é o SENHOR, e mui digno de louvor, e mais temível é do que todos os deuses. I Crônicas 16:25'),
                    ('33', 'Agora, pois, ó Deus nosso, graças Te damos,e louvamos o nome da Tua glória. I Crônicas 29:13'),
                    ('34', 'Em Ti me alegrarei e saltarei de prazer; cantarei louvores ao Teu nome, ó Altíssimo. Salmos 9:2'),
                    ('35', 'REGOZIJAI-VOS no SENHOR, vós justos, pois aos retos convém o louvor. Salmos 33:1'),
                    ('36', 'Por que estás abatida, ó minha alma, e por que te perturbas dentro de mim? Espera em Deus, pois ainda O louvarei, O Qual é a salvação da minha face, e o meu Deus. Salmos 42:11'),
                    ('37', 'Louvor e majestade há diante dEle, força e alegria no Seu lugar. I Crônicas 16:27'),
                    ('38', 'Eu louvarei ao SENHOR segundo a Sua justiça, e cantarei louvores ao nome do SENHOR altíssimo. Salmos 7:17'),
                    ('39', 'Os mansos comerão e se fartarão; louvarão ao SENHOR os que O buscam; o vosso coração viverá eternamente. Salmos 22:26'),
                    ('40', 'Louvarei ao SENHOR em todo o tempo; o Seu louvor estará continuamente na minha boca.Salmos 34:1 '),
                    ('41', 'Em Deus nos gloriamos todo o dia, e louvamos o Teu nome eternamente. Salmos 44:8'),
                    ('42', 'Farei lembrado o Teu nome de geração em geração; por isso os povos Te louvarão eternamente. Salmos 45:17'),
                    ('43', 'Para sempre Te louvarei, porque Tu o fizeste, e esperarei no Teu nome, porque é bom diante de Teus santos. Salmos 52:9'),
                    ('44', 'Preparado está o meu coração, ó Deus, preparado está o meu coração; cantarei, e darei louvores. Salmos 57:7'),
                    ('45', 'Porque a Tua benignidade é melhor do que a vida, os meus lábios Te louvarão. Salmos 63:3'),
                    ('46', 'Cantai louvores a Deus, cantai louvores; cantai louvores ao nosso Rei, cantai louvores. Salmos 47:6'),
                    ('48', 'Segundo é o Teu nome, ó Deus, assim é o Teu louvor, até aos fins da terra; a Tua mão direita está cheia de justiça. Salmos 48:10'),
                    ('49', 'Em Deus louvarei a Sua palavra, em Deus pus a minha confiança; não temerei o que me possa fazer a carne. Salmos 56:4'),
                    ('50', 'Louvar-Te-ei, Senhor, entre os povos; eu Te cantarei entre as nações.Salmos 57:9'),
                    ('51', 'A minha alma se fartará, como de tutano e de gordura; e a minha boca Te louvará com alegres lábios. Salmos 63:5'),
                    ('52', 'Pois Deus é o Rei de toda a terra, cantai louvores com inteligência. Salmos 47:7'),
                    ('53', 'Abre, Senhor, os meus lábios, e a minha boca entoará o Teu louvor. Salmos 51:15'),
                    ('54', 'Em Deus louvarei a Sua palavra; no SENHOR louvarei a Sua palavra. Salmos 56:10'),
                    ('55', 'Em Deus louvarei a Sua palavra; no SENHOR louvarei a Sua palavra. Salmos 56:10'),
                    ('56', 'Cantai a glória do Seu nome: dai glória ao Seu louvor. Salmos 66:2'),
                    ('57', 'Bendizei, povos, ao nosso Deus, e fazei ouvir a voz do Seu louvor. Salmos 66:8'),
                    ('58', 'Bendizei, ó povos, o nosso Deus; fazei ouvir a voz do seu louvor. Salmos 68:32'),
                    ('59', 'Por Ti tenho sido sustentado desde o ventre; Tu és aquele que me tiraste das entranhas de minha mãe; o meu louvor será para Ti constantemente. Salmos 71:6'),
                    ('60', 'A Ti, ó Deus, glorificamos, a Ti damos louvor, pois o Teu nome está perto, as Tuas maravilhas o declaram. Salmos 75:1'),
                    ('61', 'Bem-aventurados os que habitam em Tua casa; louvar-Te-ão continuamente. Salmos 84:4'),
                    ('62', 'Louvem-Te a Ti, ó Deus, os povos; louvem-Te os povos todos. Salmos 67:3'),
                    ('63', 'Louvarei o nome de Deus com um cântico, e engrandecê-Lo-ei com ação de graças. Salmos 69.30'),
                    ('64', 'Encha-se a minha boca do Teu louvor e da Tua glória todo o dia. Salmos 71:8'),
                    ('65', 'E eu O declararei para sempre; cantarei louvores ao Deus de Jacó. Salmos 75:9'),
                    ('66', 'Louvar-Te-ei, Senhor Deus meu, com todo o meu coração, e glorificarei o Teu nome para sempre. Salmos 86:12'),
                    ('67', 'Cantai a Deus, cantai louvores ao Seu nome; louvai Aquele que vai montado sobre os céus, pois o Seu nome é SENHOR, e exultai diante dEle. Salmos 68:4'),
                    ('68', 'Louvem-nO os céus e a terra, os rnares e tudo quanto neles se inove.Salmos 69:34'),
                    ('69', 'Mas eu esperarei continuamente, e Te louvarei cada vez mais. Salmos 71:14'),
                    ('70', 'Assim nós, Teu povo e ovelhas de Teu pasto, Te louvaremos eternamente; de geração em geração cantaremos os Teus louvores. Salmos 79:13'),
                    ('71', 'E os céus louvarão as Tuas maravilhas, ó SENHOR, a Tua fidelidade também na congregação dos santos. Salmos 89:5'),
                    ('72', 'BOM é louvar ao SENHOR. e cantar louvores ao Teu nome, ó Altíssimo. Salmos 92:1'),
                    ('73', 'Exultai no SENHOR toda a terra; exclamai e alegrai-vos de prazer e cantai louvores. Salmos 98:4'),
                    ('74', 'Louvai ao SENHOR, e invocai o Seu nome; fazei conhecidas as Suas obras entre os povos. Salmos 105:1'),
                    ('75', 'Louvem ao SENHOR pela Sua bondade. e pelas Suas maravilhas para com os filhos dos homens. Salmos 107:8'),
                    ('76', 'Louvarei grandemente ao SENHOR com a minha boca; louvá-Lo-ei entre a multidão. Salmos 109:30'),
                    ('77', 'Porque grande é o SENHOR. e digno de louvor,mais temível do que todos os deuses. Salmos 96:4'),
                    ('78', 'Louvem o Teu nome, grande e tremendo. pois é santo.Salmos 99:3'),
                    ('79', 'Louvai ao SENHOR. Louvai ao SENHOR, porque Ele é bom, porque a Sua misericórdia dura para sempre.Salmos 106:1'),
                    ('80', 'Louvai ao SENHOR. Louvarei ao SENHOR de todo o meu coração, na assembléia dos justos e na congregação.Salmos 111:1'),
                    ('81', 'Alegrai-vos, ó justos, no SENHOR, e dai louvores à memória da Sua santidade.Salmos 97:12'),
                    ('82', 'Cantarei ao SENHOR enquanto eu viver; cantarei louvores ao meu Deus, enquanto eu tiver existência.Salmos 104:33'),
                    ('83', 'Bendito seja o SENHOR Deus de Israel, de eternidade em eternidade, e todo o povo diga: Amém. Louvai ao SENHOR.Salmos 106:48'),
                    ('84', 'Louvar-Te-ei entre os povos, SENHOR, e a Ti cantarei louvores entre as nações.Salmos 108:3'),
                    ('85', 'O temor do SENHOR é o princípio da sabedoria; bom entendimento têm todos os que cumprem os Seus mandamentos; o Seu louvor permanece para sempre. Salmos 111:10'), #arquivo 6
                    ('86', 'x'),
                    ('87', 'x'),
                    ('88', 'x'),
                    ('89', 'x'),
                    ('90', 'x'),


                    ]
versiculos = dict(versiculos_lista)

vers = random.choice(list(versiculos.values()))
st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a página', ['Página 1','Página 2'])
if paginaSelecionada == 'Página 1':
    #st.image('fir.png', width=100, )
    st.markdown("<h1 style='text-align: center; color: grey;'>PROMESSAS</h1>", unsafe_allow_html=True)
    st.text_area('', vers)
    if st.button('Versículo'):
        vers = random.choice(list(versiculos.values()))
    else:
        st.write(' ')
elif paginaSelecionada == 'Página 2':
    st.title('Você selecionou a página 2')


