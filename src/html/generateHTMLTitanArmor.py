#generates html data for main.html from the json
import json

def cleanHTML(html):
    
    html = html.replace("\u2022","<br>&#8226;")
    html = html.replace("\u2014","&nbsp;&#8212&nbsp;")
    html = html.replace("\u2013","&#8211;")
    html = html.replace("\u201c","&#34;")
    html = html.replace("\u201d","&#8221;")
    html = html.replace("\u201c","&#8220;")
    html = html.replace("\u2026","...")
    
    cleanedHTML = html
    return cleanedHTML




def setHtmlVals():
    #read in the json doc
    file = open("/home/ubuntu/XurTracker/data/data.json")
    data = json.load(file)
    file.close()

    #set all vals
    week = data["Week"]
    exoticTitanLoreExt = data["Exotics"]["Titan Exotic"]["ExtLore"].replace("\n","<br>")
    exoticTitanName = data["Exotics"]["Titan Exotic"]["name"]
    exoticTitanIcon = data["Exotics"]["Titan Exotic"]["icon"]
    exoticTitanLore = data["Exotics"]["Titan Exotic"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    exoticTitanStatsList = data["Exotics"]["Titan Exotic"]["statRolls"]
    exoticTitanLoreExt = str(exoticTitanLoreExt).replace("\n","<br>")
    exoticTitanPerkIcon = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["icon"]
    exoticTitanPerkName = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["name"]
    exoticTitanPerkDesc = data["Exotics"]["Titan Exotic"]["exoticArmorPerk"][0]["desc"]


    titanHelmetName = data["Legendaries"]["Titan"]["Helmet"]["name"]
    titanHelmetLore = data["Legendaries"]["Titan"]["Helmet"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        titanHelmetLoreExt = data["Legendaries"]["Titan"]["Helmet"]["ExtLore"].replace("\n","<br>")
    except:
        titanHelmetLoreExt = data["Legendaries"]["Titan"]["Helmet"]["ExtLore"]
    titanHelmetIcon = data["Legendaries"]["Titan"]["Helmet"]["icon"]
    titanHelmetStatsList = data["Legendaries"]["Titan"]["Helmet"]["statRolls"]

    titanArmsName = data["Legendaries"]["Titan"]["Arms"]["name"]
    titanArmsLore = data["Legendaries"]["Titan"]["Arms"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        titanArmsLoreExt = data["Legendaries"]["Titan"]["Arms"]["ExtLore"].replace("\n","<br>")
    except:
        titanArmsLoreExt = data["Legendaries"]["Titan"]["Arms"]["ExtLore"]
    titanArmsIcon = data["Legendaries"]["Titan"]["Arms"]["icon"]
    titanArmsStatsList = data["Legendaries"]["Titan"]["Arms"]["statRolls"]

    titanChestName = data["Legendaries"]["Titan"]["Chest"]["name"]
    titanChestLore = data["Legendaries"]["Titan"]["Chest"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        titanChestLoreExt = data["Legendaries"]["Titan"]["Chest"]["ExtLore"].replace("\n","<br>")
    except:
        titanChestLoreExt = data["Legendaries"]["Titan"]["Chest"]["ExtLore"]
    
    titanChestIcon = data["Legendaries"]["Titan"]["Chest"]["icon"]
    titanChestStatsList = data["Legendaries"]["Titan"]["Chest"]["statRolls"]

    titanLegsName = data["Legendaries"]["Titan"]["Legs"]["name"]
    titanLegsLore = data["Legendaries"]["Titan"]["Legs"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        titanLegsLoreExt = data["Legendaries"]["Titan"]["Legs"]["ExtLore"].replace("\n","<br>")
    except:
        titanLegsLoreExt = data["Legendaries"]["Titan"]["Legs"]["ExtLore"]

    titanLegsIcon = data["Legendaries"]["Titan"]["Legs"]["icon"]
    titanLegsStatsList = data["Legendaries"]["Titan"]["Legs"]["statRolls"]

    titanMarkName = data["Legendaries"]["Titan"]["Class Item"]["name"]
    titanMarkLore = data["Legendaries"]["Titan"]["Class Item"]["lore"].replace('"','&quot').replace("\u2014","</em><br><br>&#8212&nbsp;")
    try:
        titanMarkLoreExt = data["Legendaries"]["Titan"]["Class Item"]["ExtLore"].replace("\n","<br>")
    except:
         titanMarkLoreExt = data["Legendaries"]["Titan"]["Class Item"]["ExtLore"]
    
    titanMarkIcon = data["Legendaries"]["Titan"]["Class Item"]["icon"]
    titanMarkStatsList = [0,0,0,0,0,0,0]

    loreList = [exoticTitanLoreExt,titanHelmetLoreExt,titanArmsLoreExt,titanChestLoreExt,titanLegsLoreExt,titanMarkLoreExt]

    for i in range(len(loreList)):
      if(str(loreList[i]) == "None"):
        
        if(i == 0):
            exoticTitanLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 1):
            titanHelmetLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 2):
            titanArmsLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 3):
            titanChestLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 4):
            titanLegsLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        if(i == 5):
            titanMarkLoreExt = "This weapon has no known lore. Perhaps it was lost long ago?"
        
        
        

    
    htmlTemp ="""
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>X&#251r Tracker // Titan</title>
    <link rel="shortcut icon" href="../static/favicon.ico">
    <link rel="apple-touch-icon" sizes="192x192" href="../static/favicon.ico">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    <link rel="canonical" href="https://www.xurtracker.com/titan">
    <meta charset="utf-8";>
    <meta name="description" content="Tracks Destiny 2's X&#251r location and nventory.">
    <meta name="keywords" content="xur,Xûr,Xur,xurtracker,wtfix,exotic inventory,destiny,destinythegame,whereisxur,destiny 2,D2,d2,where is xur,xur location,xurtrack,xur inventory">
    <meta name="author" content="Thomas Smith">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--Bootstrap CDN CSS-->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!--Bootstrap CDN JS-->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!--FA CDN-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <nav class="navbar navbar-expand-lg navbar-light bg-secondary text-white">
        <div class="container-fluid">
            <a class="navbar-brand mb-0 h1" href="https://www.xurtracker.com">X&#251r Tracker</a>
            <button class="navbar-toggler" style="margin-right:5px !important;" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <div class="navbar-nav">
                    <a class="nav-link active" href="all">All Items</a>
                    <a class="nav-link active" href="exotics">Exotic Items</a>
                    <a class="nav-link active" href="legendary-weapons">Legendary Weapons</a>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle active" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Armor
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                        <li><a class="dropdown-item"  aria-current="page" href="titan">Titan Armor</a></li>
                        <li><a class="dropdown-item" href="hunter">Hunter Armor</a></li>
                        <li><a class="dropdown-item" href="warlock">Warlock Armor</a></li>
                        </ul>
                    </li>
                </div>
                <nav class="navbar-nav ms-auto">
                    <div>
                        <a class="navbar-brand mb-0" href="#" target="_blank" rel="noopener noreferrer" data-bs-toggle="modal" data-bs-target="#infoModal">
                            <i class="bi bi-question-circle" style="font-size: 2rem;"></i>
                        </a>
                        <a class="navbar-brand mb-0" href="https://github.com/tlstommy/xurtracker.com" target="_blank" rel="noopener noreferrer">
                            <i class="bi bi-github" style="font-size: 2rem;"></i>
                        </a>
                        <a class="navbar-brand mb-0" href="https://twitter.com/XurTrack">
                            <i class="bi bi-twitter" style="font-size: 2rem; color: #0e1010;"></i>
                        </a>
                    </div>
                </nav>
            </div>
        </div>
    </nav> 
    <style>
        body{{
            color: #ffffff;
        }}
        .tooltip-inner {{
            background-color: #0e1010;
            box-shadow: 0px 0px 5px #ffffff;
            opacity: 1 !important;
        }}
        progress {{
            border: solid #636363 3px;
            background: #ffffff;
        }}

        progress {{
            color: #ffffff;
        }}
        progress::-moz-progress-bar {{
            background: #000000;
        }}

        progress::-webkit-progress-value {{
            background: #ffffff;
        }}

        progress::-webkit-progress-bar {{
            background: #000000;
        }}
        ::-webkit-scrollbar {{
            width: 0;
            background: transparent;
        }}
    </style>
    </head>

    <body style="background-color:  #000000; overflow: auto;">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <br>
                    <br>
                    <h1 style="text-align:center;">
                        X&#251r's Titan Armor for {week}
                        <hr>
                    </h1>
                    <br>
                    <br>
                </div>
            </div>
        </div>
        <br>            
        <br>
        <div class="container">
            <div class="row">
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th><img src="https://bungie.net/common/destiny2_content/icons/2ffa90c58bdadcca8226f553315212e7.png" class="img" width="70px" alt="exotic-warlock"></th>
                            <th><h2 style="padding-bottom: 10px;">Exotic Armorpeice</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                    <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{exoticTitanName}<hr></h2>
                    <thead>
                        <tr>
                        <th><img src="{exoticTitanIcon}" class="img" alt="exotic-warlock"></th>
                        <th>
                            <em>{exoticTitanLore}</em>
                        </th>
                        </tr>
                    </thead>
                </table>

                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <h3 style="padding-left: 1%;"><u>Exotic Perk</u></h3>
                            <th>
                                <img src="{exoticTitanPerkIcon}" style="padding-bottom: 12.5px;" class="img" alt="exotic-warlock-perk" width="75" ></img></th>
                            </th>
                            <th>
                                <h5>{exoticTitanPerkName}</h5><p>{exoticTitanPerkDesc}</p>
                            </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%;">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption><h4 style="color: #ffffff;">Stat Total : {exoticTitanStatsList[0]}</h5></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="mob" value="{exoticTitanStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="res" value="{exoticTitanStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="rec" value="{exoticTitanStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="dis" value="{exoticTitanStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="inte" value="{exoticTitanStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{exoticTitanStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="stre" value="{exoticTitanStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="titan1">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading1" style="background-color: #0e1010; border-color: #ffffff;">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse1" aria-expanded="true" aria-controls="collapse1">
                            {exoticTitanName} Lore
                        </button>
                        </h2>
                        <div id="collapse1" class="accordion-collapse collapse" aria-labelledby="heading1" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <p><h3>{exoticTitanName}</h3><hr><p>{exoticTitanLoreExt}</p></p>
                        </div>
                        </div>
                    </div>
                </div>
                <br>

              </div>
          
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <svg version="1.1" id="helmet_armor" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 51 51"  height="70" width="70" fill="#ffffff">
                                    <path d="M24.77,7.03c-8.15,0.38-14.42,7.41-14.42,15.57v16.06c0,0.23,0.13,0.44,0.34,0.53l10.33,4.68c0.78,0.35,1.66-0.22,1.66-1.07
                                        v-5.75c0,0,0,0,0,0V31.9c0-0.39-0.19-0.75-0.52-0.97l-5.39-3.64l0,0c-0.87-0.52-1.43-1.5-1.34-2.61c0.13-1.46,1.46-2.52,2.93-2.52
                                        h4.36c0.65,0,1.17,0.53,1.17,1.17v6.71c0,0,0,0.61,1.61,0.61c1.61,0,1.61-0.61,1.61-0.61v-6.71c0-0.65,0.52-1.17,1.17-1.17h4.36
                                        c1.47,0,2.8,1.06,2.93,2.52c0.1,1.11-0.47,2.09-1.34,2.61l0,0l-5.39,3.64c-0.32,0.22-0.52,0.58-0.52,0.97v5.16v5.75
                                        c0,0.85,0.88,1.42,1.66,1.07l10.33-4.68c0.21-0.1,0.34-0.3,0.34-0.53V22.17C40.66,13.56,33.47,6.62,24.77,7.03z"/>
                                </svg>
                            </th>
                            <th><h2 style="padding-bottom: 10px;">Helmet</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                    <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;">
                        <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{titanHelmetName}<hr></h2>
                        <thead>
                          <tr>
                            <th><img src={titanHelmetIcon} class="img" alt="exotic-warlock"></th>
                            <th>
                                <em>{titanHelmetLore}</em>
                            </th>
                          </tr>
                      </thead>
                    </table>
                    <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;visibility:hidden;">
                      <thead>
                          <tr>
                              <h3 style="padding-left: 1%;visibility:hidden;"><u>Exotic Perk</u></h3>
                              <th>
                                  <img src="{exoticTitanPerkIcon}" style="padding-bottom: 12.5px;" class="img" alt="exotic-warlock-perk" width="75" ></img></th>
                              </th>
                              <th>
                                  <h5>{exoticTitanPerkName}</h5><p>{exoticTitanPerkDesc}</p>
                              </th>
                          </tr>
                      </thead>
                    </table>
                    <div style="padding-left: 2%;">
                        <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                            <caption><h4 style="color: #ffffff;">Stat Total : {titanHelmetStatsList[0]}</h5></caption>
                            <thead>
                                <tr>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[1]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="mob" value="{titanHelmetStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" style="vertical-align: middle;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[2]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="res" value="{titanHelmetStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" style="vertical-align: middle;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[3]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="rec" value="{titanHelmetStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" style="vertical-align: middle;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[4]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="dis" value="{titanHelmetStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
    
                                <tr>
                                    <th scope="row" style="vertical-align: middle;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[5]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="inte" value="{titanHelmetStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
                                <tr>
                                    <th scope="row" style="vertical-align: middle;">
                                        <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                    </th>
                                    <td style="vertical-align: middle;">
                                        <h5>+{titanHelmetStatsList[6]}</h5>
                                    </td>
                                    <td style="vertical-align: middle;">
                                        
                                        <progress id="stre" value="{titanHelmetStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                        
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <br>
                    <div class="accordion" id="titan2">
                        <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                            <h2 class="accordion-header" id="heading2" style="background-color: #0e1010; border-color: #ffffff;">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse2" aria-expanded="true" aria-controls="collapse2">
                                {titanHelmetName} Lore
                            </button>
                            </h2>
                            <div id="collapse2" class="accordion-collapse collapse" aria-labelledby="heading2" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <p><h3>{titanHelmetName}</h3><hr><p>{titanHelmetLoreExt}</p></p>
                            </div>
                            </div>
                        </div>
                    </div>
                    <br>
              </div>
            </div>
        </div>
        <div class="container">
            <div class="row ">
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <svg version="1.1" id="glove_armor" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 51 51" height="70" width="70" fill="#ffffff">
                                    <path d="M40.1,30.03c0.39-0.47,0.59-1.11,0.42-1.8c-0.18-0.76-0.81-1.39-1.58-1.55c-0.81-0.17-1.54,0.14-2.01,0.68l0,0
                                        c0,0-0.03,0.04-0.05,0.07c-0.04,0.05-0.08,0.1-0.12,0.15c-0.47,0.61-1.95,2.37-3.29,2.45c-1.62,0.1,2.51-16.14,2.51-16.14l-0.01,0
                                        c0.04-0.15,0.07-0.31,0.07-0.48c0-0.98-0.79-1.77-1.77-1.77c-0.81,0-1.49,0.55-1.69,1.29l-0.01,0c0,0-0.01,0.03-0.01,0.05
                                        c-0.01,0.05-0.02,0.1-0.03,0.15c-0.24,1.21-1.68,8.2-2.81,8.89C28.48,22.77,28.5,8.79,28.5,8.79c0-0.98-0.79-1.77-1.77-1.77
                                        c-0.98,0-1.77,0.79-1.77,1.77c0,0-0.35,12.85-1.73,12.73c-1.37-0.12-2.47-10.67-2.47-10.67c0-0.98-0.79-1.77-1.77-1.77
                                        c-0.98,0-1.77,0.79-1.77,1.77c0,0.15,0.02,0.28,0.06,0.42c0.27,2.06,1.36,11.12-0.06,11.12c-1.6,0-3.68-6.35-3.68-6.35l0,0
                                        c-0.23-0.62-0.82-1.06-1.52-1.06c-0.9,0-1.62,0.73-1.62,1.62c0,0.09,0.01,0.17,0.03,0.25l-0.03,0.01c0,0,0.02,0.07,0.07,0.19
                                        c0.02,0.09,0.05,0.17,0.09,0.25c0.99,2.71,6.28,17.46,7.26,26.23c0.03,0.25,0.24,0.44,0.49,0.44h12.19c0.26,0,0.47-0.19,0.5-0.45
                                        c0.1-1.04,0.52-3.68,2.09-5.54c1.8-2.14,6.06-6.89,6.86-7.79c0.02-0.02,0.03-0.04,0.05-0.06C40.07,30.07,40.11,30.03,40.1,30.03
                                        L40.1,30.03z"/>
                                </svg>
                            </th>
                            <th><h2 style="padding-bottom: 10px;">Arms</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{titanArmsName}<hr></h2>
                    <thead>
                        <tr>
                        <th><img src={titanArmsIcon} class="img" alt="exotic-warlock"></th>
                        <th style="height: 100px;">
                            <em>{titanArmsLore}</em>
                        </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption><h4 style="color: #ffffff;">Stat Total : {titanArmsStatsList[0]}</h5></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="mob" value="{titanArmsStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="res" value="{titanArmsStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="rec" value="{titanArmsStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="dis" value="{titanArmsStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="inte" value="{titanArmsStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanArmsStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="stre" value="{titanArmsStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="titan3">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading3" style="background-color: #0e1010; border-color: #ffffff;">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse3" aria-expanded="true" aria-controls="collapse3">
                            {titanArmsName} Lore
                        </button>
                        </h2>
                        <div id="collapse3" class="accordion-collapse collapse" aria-labelledby="heading3" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <p><h3>{titanArmsName}</h3><hr><p>{titanArmsLoreExt}</p></p>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
    
              </div>
          
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <svg version="1.1" id="chest_armor" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 51 51" height="70" width="70" fill="#ffffff">
                                    <path d="M42.49,13.55c-1.06-1.51-4.05-5.05-9.52-6.49c-0.35-0.09-0.72,0.14-0.78,0.5c-0.35,2.04-1.78,8.08-6.69,8.08
                                        s-6.34-6.04-6.69-8.08c-0.06-0.36-0.43-0.59-0.78-0.5c-5.47,1.44-8.46,4.98-9.52,6.49c-0.24,0.34-0.09,0.8,0.3,0.94
                                        c2.01,0.7,7.34,2.94,7.34,7.01c0,4.24-4.47,6.89-5.87,7.61c-0.25,0.13-0.38,0.4-0.33,0.67c1.44,7.62,7.55,13.09,8.67,14.04
                                        c0.11,0.1,0.25,0.15,0.4,0.15h6.47h6.47c0.15,0,0.29-0.05,0.4-0.15c1.12-0.95,7.23-6.42,8.67-14.04c0.05-0.27-0.08-0.54-0.33-0.67
                                        c-1.4-0.72-5.87-3.37-5.87-7.61c0-4.08,5.33-6.32,7.34-7.01C42.58,14.35,42.73,13.88,42.49,13.55z"/>
                                </svg>
                            </th>
                            <th><h2 style="padding-bottom: 10px;">Chest</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{titanChestName}<hr></h2>
                    <thead>
                        <tr>
                        <th><img src="{titanChestIcon}" class="img" alt="exotic-warlock"></th>
                        <th style="height: 100px;">
                            <em>{titanChestLore}</em>
                        </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption><h4 style="color: #ffffff;">Stat Total : {titanChestStatsList[0]}</h5></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="mob" value="{titanChestStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="res" value="{titanChestStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="rec" value="{titanChestStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="dis" value="{titanChestStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="inte" value="{titanChestStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanChestStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="stre" value="{titanChestStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="titan4">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading4" style="background-color: #0e1010; border-color: #ffffff;">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse4" aria-expanded="true" aria-controls="collapse4">
                            {titanChestName} Lore
                        </button>
                        </h2>
                        <div id="collapse4" class="accordion-collapse collapse" aria-labelledby="heading4" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <p><h3>{titanChestName}</h3><hr><p>{titanChestLoreExt}</p></p>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row ">
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <svg version="1.1" id="boots_armor" xmlns="http://www.w3.org/2000/svg" x="10px" y="10px" viewBox="0 0 51 51" height="70" width="70" fill="#ffffff">
                                    <path d="M13,7.6c3.63,0,10.02,0,13.96,0c1.73,0,2.99,1.64,2.54,3.32l-5.44,20.46c-0.07,0.28,0.03,0.57,0.28,0.72
                                        c0.99,0.62,4.64,2.57,8.15,5.78c0.12,0.11,2.92-0.03,3.09-0.01c2.31,0.2,3.97-0.08,5.05,4.7c0.09,0.42-0.21,0.82-0.64,0.82
                                        c-4.21,0-24.43,0-28.17,0c-0.34,0-0.63-0.26-0.66-0.61c-0.15-1.82-0.4-7.23,1.74-9.32c0.17-0.16,0.25-0.37,0.2-0.6
                                        c-0.39-1.74-2.09-9.83-2.74-22.48C10.29,8.88,11.48,7.6,13,7.6z"/>
                                </svg>
                            </th>
                            <th><h2 style="padding-bottom: 10px;">Legs</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{titanLegsName}<hr></h2>
                    <thead>
                        <tr>
                        <th><img src="{titanLegsIcon}" class="img" alt="exotic-warlock"></th>
                        <th style="height: 100px;">
                            <em>{titanLegsLore}</em>
                        </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption><h4 style="color: #ffffff;">Stat Total : {titanLegsStatsList[0]}</h5></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="mob" value="{titanLegsStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="res" value="{titanLegsStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="rec" value="{titanLegsStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="dis" value="{titanLegsStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="inte" value="{titanLegsStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanLegsStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="stre" value="{titanLegsStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="titan5">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading5" style="background-color: #0e1010; border-color: #ffffff;">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse5" aria-expanded="true" aria-controls="collapse5">
                            {titanLegsName} Lore
                        </button>
                        </h2>
                        <div id="collapse5" class="accordion-collapse collapse" aria-labelledby="heading5" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <p><h3>{titanLegsName}</h3><hr><p>{titanLegsLoreExt}</p></p>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
    
              </div>
          
              <div class="col-md-6 border">
                <br>
                <table class="table" style="color: #ffffff;padding-left: 4.5%;">
                    <thead>
                        <tr>
                            <th>
                                <svg version="1.1" id="class_armor" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 51 51" height="70" width="70" fill="#ffffff">
                                    <path d="M43.12,7.12C38.99,9.45,25.5,9.02,25.5,9.02S12.01,9.45,7.88,7.12C7.51,6.91,7.03,7.09,6.94,7.51
                                        C6.58,9,6.07,11.93,7.03,13.37c0.09,0.13,0.22,0.21,0.38,0.25c1.23,0.3,7.36,1.65,18.09,1.65c10.73,0,16.86-1.35,18.09-1.65
                                        c0.15-0.04,0.29-0.12,0.38-0.25c0.96-1.44,0.45-4.37,0.1-5.86C43.97,7.09,43.49,6.91,43.12,7.12z"/>
                                    <g>
                                        <path d="M9.27,28.34c0,0,0,2.34,2.27,2.34s2.27-2.34,2.27-2.34V15.73c-1.93-0.22-3.45-0.45-4.55-0.65V28.34z"/>
                                        <path d="M16.3,34.8c0,0,0,2.34,2.27,2.34s2.27-2.34,2.27-2.34V16.24c-1.66-0.06-3.18-0.16-4.55-0.27V34.8z"/>
                                        <path d="M37.18,28.34c0,0,0,2.34,2.27,2.34s2.27-2.34,2.27-2.34V15.08c-1.09,0.2-2.61,0.44-4.55,0.65V28.34z"/>
                                        <path d="M30.15,34.8c0,0,0,2.34,2.27,2.34s2.27-2.34,2.27-2.34V15.97c-1.36,0.11-2.88,0.21-4.55,0.27V34.8z"/>
                                        <path d="M23.23,16.31v25.31c0,0,0,2.34,2.27,2.34s2.27-2.34,2.27-2.34V16.31c-0.74,0.01-1.49,0.02-2.27,0.02
                                            C24.72,16.34,23.96,16.33,23.23,16.31z"/>
                                    </g>
                                </svg>
                            </th>
                            <th><h2 style="padding-bottom: 10px;">Titan Mark</h2></th>
                        </tr>
                    </thead>
                </table>
                <br>
                <table class="table table-borderless" style="color: #ffffff;padding-left: 4.5%;height: 100px;">
                    <h2 style="text-align: center; border-bottom: #ffffff; border: #ffffff;">{titanMarkName}<hr></h2>
                    <thead>
                        <tr>
                        <th><img src="{titanMarkIcon}" class="img" alt="exotic-warlock"></th>
                        <th style="height: 100px;">
                            <em>{titanMarkLore}</em>
                        </th>
                        </tr>
                    </thead>
                </table>
                <div style="padding-left: 2%">
                    <table class="table table-borderless" style="color: #ffffff;max-width: 200px;">
                        <caption style="height: 53px;">Titan Marks do not have randomized stats.<br></caption>
                        <thead>
                            <tr>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row" style="vertical-align: middle;border: so #ffffff;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/e26e0e93a9daf4fdd21bf64eb9246340.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Mobility <br>Increases movement speed and maximum jump height."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[1]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="mob" value="{titanMarkStatsList[1]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/202ecc1c6febeb6b97dafc856e863140.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Resilience <br>&#8226Decreases cooldown of Class abilities.<br>&#8226;Increases Shield capacity.<br>&#8226;Reduces incoming damage."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[2]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="res" value="{titanMarkStatsList[2]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/128eee4ee7fc127851ab32eac6ca91cf.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Recovery<br>Increases health regeneration rate."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[3]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="rec" value="{titanMarkStatsList[3]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/79be2d4adef6a19203f7385e5c63b45b.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Discipline<br>Decreases cooldown of grenade abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[4]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="dis" value="{titanMarkStatsList[4]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>

                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/d1c154469670e9a592c9d4cbdcae5764.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Intellect<br>Decreases cooldown of Super abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[5]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="inte" value="{titanMarkStatsList[5]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                            <tr>
                                <th scope="row" style="vertical-align: middle;">
                                    <img src="https://www.bungie.net/common/destiny2_content/icons/ea5af04ccd6a3470a44fd7bb0f66e2f7.png" class="img"alt="exotic-warlock-perk" width="50" data-bs-toggle="tooltip" data-bs-html="true" data-bs-placement="left" title="Strength<br>Decreases cooldown of melee abilities."></img>
                                </th>
                                <td style="vertical-align: middle;">
                                    <h5>+{titanMarkStatsList[6]}</h5>
                                </td>
                                <td style="vertical-align: middle;">
                                    
                                    <progress id="stre" value="{titanMarkStatsList[6]}" max="40" style="height: 30px; width: 200px;"> 32% </progress>
                                    
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <br>
                <div class="accordion" id="titan6">
                    <div class="accordion-item" style="background-color: #0e1010; border-color: #ffffff;">
                        <h2 class="accordion-header" id="heading6" style="background-color: #0e1010; border-color: #ffffff;">
                        <button class="accordion-button" type="button" data-bs-toggle="collapse" style="background-color: #0e1010; color: #ffffff;" data-bs-target="#collapse6" aria-expanded="true" aria-controls="collapse6">
                            {titanMarkName} Lore
                        </button>
                        </h2>
                        <div id="collapse6" class="accordion-collapse collapse" aria-labelledby="heading6" data-bs-parent="#accordionExample">
                        <div class="accordion-body">
                            <p><h3>{titanMarkName}</h3><hr><p>{titanMarkLoreExt}</p></p>
                        </div>
                        </div>
                    </div>
                </div>
                <br>
                </div>
            </div>
        </div>
        <br>
        <br>
        <footer class="bg-dark text-center text-white">
            <div class="text-center p-3" style="background-color:#6e757d;">
              Created By:
              <a class="text-white" href="https://www.linkedin.com/in/thomas-smith-89a918192/">Thomas Smith</a> // Bungie Net: <a class="text-white" href="https://www.bungie.net/7/en/User/Profile/254/10061778?bgn=Lulamae1">Lulamae1#6072</a>
            </div>
        </footer>
        <!--Help Modal -->
        <div class="modal fade" id="infoModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" style="color:#000000">
        <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">X&#251r Tracker - Help</h5>
            <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">
                    <i class="bi bi-x-lg"></i>
                </span>
            </button>
            </div>
            <div class="modal-body">
                <h4>Thanks for using X&#251r Tracker!</h4>
                <hr>
                <p>
                    <h6>
                        &#8226;Hover over an item for more information. <br><br>
                        &#8226;Yellow borders indicate a favorable perk.<br><br>
                        &#8226;Pages for each type of item (i.e. Exoitc Items, Legendary Weapons), offer more detailed data.<br><br>
                        <br> Have an issue or suggestion? Please submit it <a href="https://github.com/tlstommy/xurtracker.com/issues">here!</a>
                        
                    </h6>
                </p>
            </div>
        </div>
        </div>
        </div>
        <script>
            var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
            var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {{
                return new bootstrap.Popover(popoverTriggerEl)
            }})
            
            var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
            var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {{
                return new bootstrap.Tooltip(tooltipTriggerEl)
            }})
        </script>
    </body>
    </html>
    """.format(week=week,exoticTitanLoreExt=exoticTitanLoreExt,exoticTitanName=exoticTitanName,exoticTitanIcon=exoticTitanIcon,exoticTitanLore=exoticTitanLore,exoticTitanStatsList=exoticTitanStatsList,
    titanHelmetLoreExt=titanHelmetLoreExt,titanHelmetName=titanHelmetName,titanHelmetIcon=titanHelmetIcon,titanHelmetLore=titanHelmetLore,titanHelmetStatsList=titanHelmetStatsList,
    titanArmsLoreExt=titanArmsLoreExt,titanArmsName=titanArmsName,titanArmsIcon=titanArmsIcon,titanArmsLore=titanArmsLore,titanArmsStatsList=titanArmsStatsList,
    titanChestLoreExt=titanChestLoreExt,titanChestName=titanChestName,titanChestIcon=titanChestIcon,titanChestLore=titanChestLore,titanChestStatsList=titanChestStatsList,
    titanLegsLoreExt=titanLegsLoreExt,titanLegsName=titanLegsName,titanLegsIcon=titanLegsIcon,titanLegsLore=titanLegsLore,titanLegsStatsList=titanLegsStatsList,
    titanMarkLoreExt=titanMarkLoreExt,titanMarkName=titanMarkName,titanMarkIcon=titanMarkIcon,titanMarkLore=titanMarkLore,titanMarkStatsList=titanMarkStatsList,exoticTitanPerkIcon=exoticTitanPerkIcon,exoticTitanPerkName=exoticTitanPerkName,exoticTitanPerkDesc=exoticTitanPerkDesc)

    
    htmlTemp = cleanHTML(htmlTemp)
    text_file = open("/home/ubuntu/XurTracker/templates/titan_armor.html", "w")
    text_file.write(htmlTemp)
    text_file.close()



setHtmlVals()