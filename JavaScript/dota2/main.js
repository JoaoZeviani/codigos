var allHeroes = [];

function logHero(hero) {
    var heroDiv = document.createElement('div');
    heroDiv.style.border = '1px solid black';
    heroDiv.style.margin = '10px';
    heroDiv.style.padding = '10px';

    // Create an img element for the hero image
    var heroImg = document.createElement('img');

    // Set the src attribute to the URL of the image
    heroImg.src = 'https://cdn.dota2.com/apps/dota2/images/heroes/' + hero.name.replace('npc_dota_hero_', '') + '_full.png';

    // Append the img element to the heroDiv
    heroDiv.appendChild(heroImg);

    heroDiv.innerHTML += '<br>' + 
        'Hero Name: ' + hero.localized_name + '<br>' +
        'Hero Attribute: ' + hero.getPrimaryAttrFullName() + '<br>' +
        'Hero Attack Type: ' + hero.attack_type + '<br>' +
        'Roles: ' + hero.roles.join(', ');
    document.getElementById('log').appendChild(heroDiv);
}

function logFilteredHeroes() {
    // Clear the log div
    document.getElementById('log').innerHTML = '';

    // Get the selected attributes
    var attributes = ['str', 'agi', 'int', 'all'].filter(attr => document.getElementById(attr).checked);

    // Get the selected roles
    var roles = ['Initiator', 'Durable', 'Disabler', 'Carry', 'Nuker', 'Escape', 'Pusher'].filter(role => document.getElementById(role).checked);

    // Log the heroes with the selected attributes and roles
    for (let i = 0; i < allHeroes.length; i++) {
        if (attributes.includes(allHeroes[i].primary_attr) &&
            roles.every(role => allHeroes[i].roles.includes(role))) {
            logHero(allHeroes[i]);
        }
    }
}

// Define the API URL
const apiUrl = 'https://api.opendota.com/api/heroes';

// Make a GET request to the API
fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response failed');
        }
        return response.json();
    })
    .then(data => {
        data.forEach(hero => {
            const newHero = new Hero(hero.id, hero.localized_name, hero.name, hero.primary_attr, hero.attack_type, hero.roles)
            allHeroes.push(newHero);
        });
    })
    .catch(error => {
        document.getElementById('log').append(error);
    });
