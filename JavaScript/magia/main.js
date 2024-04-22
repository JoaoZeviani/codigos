var pontos = 20;

var forca = 0;
var agilidade = 0;
var inteligencia = 0;

var forcaAdicional = 0;
var agilidadeAdicional = 0;
var inteligenciaAdicional = 0;

var vida = 1;
var iniciativa = 1;
var mana = 1;

var vidaAdicional = 0;
var iniciativaAdicional = 0;
var manaAdicional = 0;

function atualizar() {
    // Reset base attributes
    forca = parseInt(document.getElementById('forca').innerText);
    agilidade = parseInt(document.getElementById('agilidade').innerText);
    inteligencia = parseInt(document.getElementById('inteligencia').innerText);

    vidaAdicional = 0;
    iniciativaAdicional = 0;
    manaAdicional = 0;
    
    forcaAdicional = 0;
    agilidadeAdicional = 0;
    inteligenciaAdicional = 0;

    // Iterate over all items
    for (var i = 1; i <= itens.length; i++) {
        var item = itens.find(item => item.id === i);
        // If the item is purchased, add its attributes to the player's attributes
        if (item.comprado) {
            if (item.forca) {
                forcaAdicional += item.forca;
            }
            if (item.agilidade) {
                agilidadeAdicional += item.agilidade;
            }
            if (item.inteligencia) {
                inteligenciaAdicional += item.inteligencia;
            }
            if (item.vida) {
                vidaAdicional += item.vida;
            }
            if (item.iniciativa) {
                iniciativaAdicional += item.iniciativa;
            }
            if (item.mana) {
                manaAdicional += item.mana;
            }
        } 
    }

    document.getElementById('forca').innerText = forca + ' + ' + forcaAdicional;
    document.getElementById('agilidade').innerText = agilidade + ' + ' + agilidadeAdicional;
    document.getElementById('inteligencia').innerText = inteligencia + ' + ' + inteligenciaAdicional;

    vida = forca != 0 ? 10 * (forca + forcaAdicional) : 1;
    iniciativa = agilidade != 0 ? 10 * (agilidade + agilidadeAdicional) : 1;
    mana = inteligencia != 0 ? 10 * (inteligencia + inteligenciaAdicional) : 1;

    document.getElementById('vida').innerText = vida + ' + ' + vidaAdicional;
    document.getElementById('iniciativa').innerText = iniciativa + ' + ' + iniciativaAdicional;
    document.getElementById('mana').innerText = mana + ' + ' + manaAdicional;

    document.getElementById('pontos').innerText = pontos;

    atualizarItens();
}

function alterarAtributo(atributo, valor) {
    var input = document.getElementById(atributo);
    var novoValor = parseInt(input.innerText) || 0;

    novoValor += valor;

    if (novoValor < 0 || pontos - valor < 0) {
        return;
    }

    input.innerText = novoValor;
    pontos -= valor;
    atualizar();
}

function atualizarItens() {
    var itensLoja = document.getElementById('itensLoja');
    // esvaziar tabela
    while (itensLoja.rows.length > 0) {
        itensLoja.deleteRow(0);
    }

    var meusItens = document.getElementById('meusItens');
    // esvaziar tabela
    while (meusItens.rows.length > 0) {
        meusItens.deleteRow(0);
    }

    // Para cada item existente
    for (var i = 1; i <= itens.length; i++) {
        var item = itens.find(item => item.id === i);

        // Se ele nao estiver comprado, adicione ele para a tabela itensLoja
        if (item.comprado == false) {
            var linha = itensLoja.insertRow(-1);

            var celulaFoto = linha.insertCell(0);
            var celulaNome = linha.insertCell(1);
            var celulaCusto = linha.insertCell(2);
            var celulaDescricao = linha.insertCell(3);
            var celulaBotao = linha.insertCell(4);

            celulaFoto.innerHTML = '<img src="FotosItens/' + item.nome + '.jfif" style="width:70px;height:70px;">';
            celulaNome.innerHTML = item.nome;
            celulaCusto.innerHTML = item.custo;

            var descricao = '';

            for (var prop in item) {
                if (prop !== 'nome' && prop !== 'custo' && prop !== 'comprado' && prop !== 'id') {
                    descricao += prop + ': ' + item[prop] + '<br>';
                }
            }

            celulaDescricao.innerHTML = descricao;

            celulaBotao.innerHTML = '<button onclick="comprarItem(' + i + ')">Comprar</button>';

        } else { // Se ele estiver comprado, adicione ele para a tabela meusItens
            var linha = meusItens.insertRow(-1);

            var celulaFoto = linha.insertCell(0);
            var celulaNome = linha.insertCell(1);
            var celulaCusto = linha.insertCell(2);
            var celulaDescricao = linha.insertCell(3);
            var celulaBotao = linha.insertCell(4);

            celulaFoto.innerHTML = '<img src="FotosItens/' + item.nome + '.jfif" style="width:70px;height:70px;">';
            celulaNome.innerHTML = item.nome;
            celulaCusto.innerHTML = item.custo;

            var descricao = '';

            for (var prop in item) {
                if (prop !== 'nome' && prop !== 'custo' && prop !== 'comprado' && prop !== 'id') {
                    descricao += prop + ': ' + item[prop] + '<br>';
                }
            }

            celulaDescricao.innerHTML = descricao;

            celulaBotao.innerHTML = '<button onclick="venderItem(' + i + ')">Vender</button>';
        }


    }

}

function comprarItem(id) {
    var item = itens.find(item => item.id === id);

    if (pontos >= item.custo) {
        // Subtrai o custo do item dos pontos do personagem
        pontos -= item.custo;

        // Muda o status comprado para true
        item.comprado = true;

        // Atualizar a tabela dos itens
        atualizar()
    }
}

function venderItem(id) {
    var item = itens.find(item => item.id === id);

    // Soma o custo do item aos pontos do personagem
    pontos += item.custo;

    // Muda o status comprado para false
    item.comprado = false;

    // Atualizar a tabela dos itens
    atualizar()

}

function atualizarHabilidades() {
    var listaHabilidades = document.getElementById('habilidades');

    // Para cada habilidade existente
    for (var i = 1; i <= habilidades.length; i++) {
        var habilidade = habilidades.find(habilidade => habilidade.id === i);

        // adicione ele para a tabela Habilidades
        var linha = listaHabilidades.insertRow(-1);

        var celulaNome = linha.insertCell(0);
        var celulaDescricao = linha.insertCell(1);

        celulaNome.innerHTML = habilidade.nome;
        celulaDescricao.innerHTML = habilidade.descricao;
    }

}

atualizar();
atualizarHabilidades()
