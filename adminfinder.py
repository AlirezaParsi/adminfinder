#!/usr/bin/python2
# This was written for educational purpose only. Use it at your own risk.
# Author will be not responsible for any damage!
################################################################# 

import httplib
import socket
import sys


try:
    print "\t################################################################"
    print "\t#           TCJ ADMIN PAGE FINDER TOOL (Version 1.6)           #"
    print "\t#                         T.H.C Team                           #"
    print "\t#                https://www.t.me/thcsecurity                  #"
    print "\t#                                                              #"
    print "\t#                      Edited By Aliza                         #"
    print "\t################################################################"
    var1=0
    var2=0

    php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','siteadmin/login.htm','admin/account.html','admin/account.htm','admin/index.html','admin/index.htm','admin/login.html','admin/login.htm','admin/admin.html','admin/admin.htm',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/login.htm','admin_area/index.html','admin_area/index.htm','admin/controlpanel.php','admin.php','admincp/index.php','admincp/login.php','admincp/index.html','admincp/index.htm','admin/account.html','admin/account.htm','adminpanel.html','adminpanel.htm','webadmin.html','webadmin.htm',
'webadmin/index.html','webadmin/index.htm','webadmin/admin.html','webadmin/admin.htm','webadmin/login.html','webadmin/login.htm','admin/admin_login.html','admin/admin_login.htm','admin_login.html','admin_login.htm','panel-administracion/login.html','panel-administracion/login.htm',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','admin_area/admin.htm','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/index.htm','bb-admin/login.html','bb-admin/login.htm','acceso.php','bb-admin/admin.html','bb-admin/admin.htm','admin/home.html','admin/home.htm','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','pages/admin/admin-login.htm','admin/admin-login.html','admin/admin-login.htm','admin-login.html','admin-login.htm','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','admin/adminLogin.htm','adminLogin.html','adminLogin.htm','admin/adminLogin.html','admin/adminLogin.htm','home.html','home.htm','rcjakar/admin/login.php','adminarea/index.html','adminarea/index.htm','adminarea/admin.html','adminarea/admin.htm',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin/controlpanel.htm','administrator/controlpanel.php','administrator/controlpanel.html','administrator/controlpanel.htm','admin.html','admin.htm','admin/cp.html','admin/cp.htm','cp.html','cp.html','adminpanel.php','moderator.html','moderator.htm',
'administrator/index.html','administrator/index.htm','administrator/login.html','administrator/login.htm','user.html','user.htm','administrator/account.html','administrator/account.htm','administrator.html','administrator.htm','login.html','login.htm','modelsearch/login.html','modelsearch/login.htm',
'moderator/login.html','moderator/login.htm','adminarea/login.html','adminarea/login.htm','panel-administracion/index.html','panel-administracion/index.htm','panel-administracion/admin.html','panel-administracion/admin.htm','modelsearch/index.html','modelsearch/index.htm','modelsearch/admin.html','modelsearch/admin.htm',
'admincontrol/login.html','admincontrol/login.htm','adm/index.html','adm/index.htm','adm.html','adm.htm','moderator/admin.html','moderator/admin.htm','moderator/admin.htm','user.php','account.html','account.htm','controlpanel.html','controlpanel.htm','admincontrol.html','admincontrol.htm',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','kpanel/','cpadmin.php','admin/cpadmin.php','administrator/cpadmin.php','adminpage/cpadmin.php','admin-page/cpadmin.php','user/cpadmin.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','secur-login.php','wp-admin/','administrator/login.html','login/','log-in.php','member.php','cpmember.php','cp-member.php','member.html','cpmember.html','cp-member.html','member.htm','cpmember.htm',
'cp-member.htm','sign_in.php','sign-in.php','signin.php','accounts.php','relogin.php','check.php','blog/wp-login.php','processlogin.php','checklogin.php','checkuser.php','checkadmin.php','isadmin.php','authenticate.php','authentication.php','auth.php','authuser.php','authadmin.php','fileadmin.php','sysadmin.php','yonetim.php','yonetici.php','ur-admin.php','administr8.php','websiteadmin.php','admins.php','pages/administrator/admin-login.php','pages/administrator/admin.php','pages/administrator/login.php','pages/admin/login.php','pages/admin/admin.php','admincp/admin-login.php',
'vorod.php','voroud.php','vorud.php','join.php','admincp/join.php','admin/join.php','administrator/join.php','webmaster.php','autologin.php','userlogin.php','userjoin.php','user-login.php','admincp/user-login.php','admin-cp/user-login.php','administrator/user-login.php','admincp/user-join.php','admin-cp/user-join.php','administrator/user-join.php','cmsadmin.php','yonetici.php','cgi-bin/login.php','login1.php','login_admin.php','login_out/','login_out.php','login_user.php','loginsuper.php','super1.php','super_index.php','super_login.php','super_join.php','supermanager.php','superman.php','superuser.php','supervise/Login.php','letmein.php','superuser.php','sysadm.php','access.php',
'mn-admin/index.php','mn-admin/login.php','mn-admin/admin.php','security/','admini/','letmein','admin_user/','admin_users','0admin/login.php','0manager/admin.php','a_main.php','aaa.php','aadmin/','abc/','acct/login.php','d_admin/admin_login.php',
'ad_login/','ad_login.php','add_admin/','add_user/','addfile.php','addmember/','addmember.php','adduser/','adduser.php','admanage/','adminpro/','adminmember.php','adminmember/','admins/','adsystem/index.php','adsystem/login.php','adsystem/admin.php','myadmin/','myadmin/login.php','myadmin/admin.php','my-admin/','my-admin/admin.php','my-admin/login.php','yonetim.php','indy_admin/','liveUser_admin/','lotus_domino_admin/','p/w/','psuser/','personal/','accounts/',
'acesso/','acesso.php','banneradmin/','cadmins/','ccms/','ccms/index.php','ccms/login.php','ccp14admin/','cms/','config/','configuration/','configure/','customer_login/','dir-login/','directadmin/','donos/','edit/','ezsqliteadmin/','fileadmin/','formslogin/','funcoes/','globes_admin/','hpwebjetadmin/','irc-macadmin/','joomla/administrator/','login-us/','login-redirect/','macadmin/','maintenance/','manage/','management.php',
'manager/','manuallogin/','members/','members.php','membro/','membros/','memlogin/','meta_login/','modcp/','navsiteadmin/','newsadmin/','newsadmin.php','news-admin/','news-admin.php','funadmin/','fun-admin/','funadmin.php/','fun-admin.php','nsw/admin/login.php','openvpnadmin/','painel/','panelc/','paneldecontrol/','passe/','password/','pgadmin/','php/','phpsqliteadmin/','phpldapadmin/','platz_login/','power_user/',
'processlogin/','project-admins/','pureadmin/','radmind-1/','raiz/','rcLogin/','registration/','root/','root/login.php','root/admin.php','roots/','roots/admin.php','roots/login.php','saff/','secret/','secrets/','secure/','senha/','senhas/','server_admin_small/','showlogin/','sff/','simplelogin/','sistema/','siteadmin/login.php','siteadmin/admin.php','smblogin/','sql-admin/','ss_vms_admin_sm/','sshadmin/','staradmin/','sub-login/','superman/','administrator/?h','GeneratedItems/','sw/','dynpoll/admin/','mailer/admin/',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews',
'0admin/','0manager/','AdminTools/','Clave/','Database_Administration/','FCKeditor/editor/images/anchor.gif','server.php','Server/','ServerAdministrator/','Sing/','Super-Admin/','SysAdmin/','SysAdmin2/','UserLogin/','access/','acct_login/','admcp/','admin.xhtml','admin1.php','admin4_account/','admin4_colon/','admincontrol/','admincp/','administer/','administr8/','administracao/','administratie/',
'administration.php','administratie.php','administration/','administratoraccounts/','administrators.php','administrators/','administrivia/','modiriyat/','modiriat/','modiryat/','modiriyat/modiriyat.php','modiriyat/modiriat.php','modiriyat/modiryat.php','modiriat/admin.php','modiryat/login.php','adminitem.php',
'adminitem/','adminitems.php','adminpanel/','adminsite/','admistrador','admistrador/','admon/','autologin/','blogindex/','cgi-bin/login','cgi-bin/loginphp','cmsadmin/','control.php','control/','controle','controle/','controles','controles/','controlpanel','controlpanel/','cp','cp/','cpanel','cpanel_file/','index.swf',
'instadmin','instadmin/','irectadmin/','key/','letmein/','log-in/','log_in.php','log_in/','login','login-ir/','login-fa/','login1','login1/','login1php','login_admin','login_admin/','login_db/','login_out','login_user','login_user/','loginerror/','loginflat/','loginok/','loginsave/','loginsuper','loginsuper/','logo_sysadmin/','logout/','hall7/admin.php',
'logoutphp','manage.php','management/','manager.php','member/','moderatorcp','modules/admin/','net/','news_detail.php','not/','noticias/','pages/admin/','panel.php','panel/','phppgadmin/','radmind/','raiz','roots','siteadmin/','super','super/','super1','super1/','super1php','super_index','super_index/','super_indexphp','super_loginphp','superphp','superphp/','superman','supermanagerphp','supermanagerphp/',
'supermanphp','supermanphp/','super.php','superuser','superuser/','superuserphp','superuserphp/','supervise/','supervise/Login','supervise/Loginphp','supervise/Loginphp/','supervisor/','support_login/','sys-admin/',
'sysadm/','sysadmins/','system-administration/','typo3/','usager/','user/','useradmin/','username/','users.php','users/','usr/','usuario','utility_login/','uvpanel/','vadmind/','vmailadmin/','vorod/','voroud/','vorud/','webadmin','webmaster/','websvn/','wizmysqladmin/','wp-admin','wp-login/','xlogin/',
'_admin','backoffice','backoffice/','modcp.php','modcp/admin.php','modcp/modcp.php','modcp/login.php','pages/service-login.php']

    asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.asp','admin/account.aspx','admin/index.asp','admin/index.aspx','admin/login.asp','admin/login.aspx','admin/admin.asp','admin/admin.aspx',
'admin_area/admin.asp','admin_area/admin.aspx','admin_area/login.asp','admin_area/login.aspx','siteadmin/login.asp','siteadmin/login.aspx','siteadmin/index.asp','siteadmin/index.aspx','siteadmin/login.html','siteadmin/login.htm','admin/account.html','admin/account.htm','admin/index.html','admin/index.htm','admin/login.html','admin/login.htm','admin/admin.html','admin/admin.htm',
'admin_area/index.asp','admin_area/index.aspx','bb-admin/index.asp','bb-admin/index.aspx','bb-admin/login.asp','bb-admin/login.aspx','bb-admin/admin.asp','bb-admin/admin.asp','admin/home.asp','admin/home.aspx','admin_area/login.html','admin_area/login.htm','admin_area/index.html','admin_area/index.htm','admin/controlpanel.asp','admin/controlpanel.aspx','admin.asp','admin.aspx','admincp/index.asp','admincp/index.aspx','admincp/login.asp','admincp/login.aspx','admincp/index.html','admincp/index.htm','admin/account.html','admin/account.htm','adminpanel.html','adminpanel.htm','webadmin.html','webadmin.htm',
'webadmin/index.html','webadmin/index.htm','webadmin/admin.html','webadmin/admin.htm','webadmin/login.html','webadmin/login.htm','admin/admin_login.html','admin/admin_login.htm','admin_login.html','admin_login.htm','panel-administracion/login.html','panel-administracion/login.htm',
'admin/cp.asp','admin/cp.aspx','cp.asp','cp.aspx','administrator/index.asp','administrator/index.aspx','nsw/admin/login.asp','nsw/admin/login.aspx','webadmin/login.asp','webadmin/login.aspx','admin/admin_login.asp','admin/admin_login.aspx','admin_login.asp','admin_login.aspx',
'administrator/account.asp','administrator/account.aspx','administrator.asp','administrator.aspx','admin_area/admin.html','admin_area/admin.htm','pages/admin/admin-login.asp','pages/admin/admin-login.aspx','admin/admin-login.asp','admin/admin-login.aspx','admin-login.asp','admin-login.aspx',
'bb-admin/index.html','bb-admin/index.htm','bb-admin/login.html','bb-admin/login.htm','acceso.asp','acceso.aspx','bb-admin/admin.html','bb-admin/admin.htm','admin/home.html','admin/home.htm','login.asp','login.aspx','modelsearch/login.asp','modelsearch/login.aspx','moderator.asp','moderator.aspx','moderator/login.asp','moderator/login.aspx',
'moderator/admin.asp','moderator/admin.aspx','account.asp','account.aspx','pages/admin/admin-login.html','pages/admin/admin-login.htm','admin/admin-login.html','admin/admin-login.htm','admin-login.html','admin-login.htm','controlpanel.asp','controlpanel.aspx','admincontrol.asp','admincontrol.aspx',
'admin/adminLogin.html','admin/adminLogin.htm','adminLogin.html','adminLogin.htm','admin/adminLogin.html','admin/adminLogin.htm','home.html','home.htm','rcjakar/admin/login.asp','rcjakar/admin/login.aspx','adminarea/index.html','adminarea/index.htm','adminarea/admin.html','adminarea/admin.htm',
'webadmin.asp','webadmin.aspx','webadmin/index.asp','webadmin/index.aspx','webadmin/admin.asp','webadmin/admin.aspx','admin/controlpanel.html','admin/controlpanel.htm','admin/controlpanel.asp','admin/controlpanel.aspx','administrator/controlpanel.asp','administrator/controlpanel.aspx','administrator/controlpanel.html','administrator/controlpanel.htm','admin.html','admin.htm','admin/cp.html','admin/cp.htm','cp.html','cp.html','adminpanel.asp','adminpanel.aspx','moderator.html','moderator.htm',
'administrator/index.html','administrator/index.htm','administrator/login.html','administrator/login.htm','user.html','user.htm','administrator/account.html','administrator/account.htm','administrator.html','administrator.htm','login.html','login.htm','modelsearch/login.html','modelsearch/login.htm',
'moderator/login.html','moderator/login.htm','adminarea/login.html','adminarea/login.htm','panel-administracion/index.html','panel-administracion/index.htm','panel-administracion/admin.html','panel-administracion/admin.htm','modelsearch/index.html','modelsearch/index.htm','modelsearch/admin.html','modelsearch/admin.htm',
'admincontrol/login.html','admincontrol/login.htm','adm/index.html','adm/index.htm','adm.html','adm.htm','moderator/admin.html','moderator/admin.htm','moderator/admin.htm','user.asp','user.aspx','account.html','account.htm','controlpanel.html','controlpanel.htm','admincontrol.html','admincontrol.htm',
'panel-administracion/login.asp','panel-administracion/login.aspx','wp-login.asp','wp-login.aspx','adminLogin.asp','adminLogin.aspx','admin/adminLogin.asp','admin/adminLogin.aspx','home.asp','home.aspx','adminarea/index.asp','adminarea/index.aspx',
'adminarea/admin.asp','adminarea/admin.aspx','adminarea/login.asp','adminarea/login.aspx','panel-administracion/index.asp','panel-administracion/index.aspx','panel-administracion/admin.asp','panel-administracion/admin.aspx','modelsearch/index.asp','modelsearch/index.aspx',
'modelsearch/admin.asp','modelsearch/admin.aspx','admincontrol/login.asp','admincontrol/login.aspx','adm/admloginuser.asp','adm/admloginuser.aspx','admloginuser.asp','admloginuser.aspx','admin2.asp','admin2.aspx','admin2/login.asp','admin2/login.aspx','admin2/index.asp','admin2/index.aspx','usuarios/login.asp','usuarios/login.aspx',
'adm/index.asp','adm/index.aspx','adm.asp','adm.aspx','kpanel/','cpadmin.asp','cpadmin.aspx','admin/cpadmin.asp','admin/cpadmin.aspx','administrator/cpadmin.asp','administrator/cpadmin.aspx','adminpage/cpadmin.asp','adminpage/cpadmin.aspx','admin-page/cpadmin.asp','admin-page/cpadmin.aspx','user/cpadmin.asp','user/cpadmin.aspx','adm_auth.asp','adm_auth.aspx','memberadmin.asp','memberadmin.aspx','administratorlogin.asp','administratorlogin.aspx','secur-login.asp','secur-login.aspx','administrator/login.html','login/','log-in.asp','log-in.aspx','member.asp','member.aspx','cpmember.asp','cpmember.aspx','cp-member.asp','cp-member.aspx','member.html','cpmember.html','cp-member.html','member.htm','cpmember.htm',
'cp-member.htm','sign_in.asp','sign_in.aspx','sign-in.asp','sign-in.aspx','signin.asp','signin.aspx','accounts.asp','accounts.aspx','relogin.asp','relogin.aspx','check.asp','check.aspx','blog/wp-login.asp','blog/wp-login.aspx','blog/login.asp','blog/wp-login.aspx','processlogin.asp','processlogin.aspx','checklogin.asp','checklogin.aspx','checkuser.asp','checkuser.aspx','checkadmin.asp','checkadmin.aspx','isadmin.asp','isadmin.aspx','authenticate.asp','authenticate.aspx','authentication.asp','authentication.aspx','auth.asp','auth.aspx','authuser.asp','authuser.aspx','authadmin.asp','authadmin.aspx','fileadmin.asp','fileadmin.aspx','sysadmin.asp','sysadmin.aspx','yonetim.asp','yonetim.aspx','yonetici.asp','yonetici.aspx','ur-admin.asp','ur-admin.aspx','administr8.asp','administr8.aspx','websiteadmin.asp','websiteadmin.aspx','admins.asp','admins.aspx','pages/administrator/admin-login.asp','pages/administrator/admin-login.aspx','pages/administrator/admin.asp','pages/administrator/admin.aspx','pages/administrator/login.asp','pages/administrator/login.aspx','pages/admin/login.asp','pages/admin/login.aspx','pages/admin/admin.asp','pages/admin/admin.aspx','admincp/admin-login.asp','admincp/admin-login.aspx','affiliate.asp','affiliate.aspx',
'vorod.asp','vorod.aspx','voroud.asp','voroud.aspx','vorud.asp','vorud.aspx','join.asp','join.aspx','admincp/join.asp','admincp/join.aspx','admin/join.asp','admin/join.aspx','administrator/join.asp','administrator/join.aspx','webmaster.asp','webmaster.aspx','autologin.asp','autologin.aspx','userlogin.asp','userlogin.aspx','userjoin.asp','userjoin.aspx','user-login.asp','user-login.aspx','admincp/user-login.asp','admincp/user-login.aspx','admin-cp/user-login.asp','admin-cp/user-login.aspx','administrator/user-login.asp','administrator/user-login.aspx','admincp/user-join.asp','admincp/user-join.aspx','admin-cp/user-join.asp','admin-cp/user-join.aspx','administrator/user-join.asp','administrator/user-join.aspx','cmsadmin.asp','cmsadmin.aspx','cgi-bin/login.asp','cgi-bin/login.aspx','login1.asp','login1.aspx','login_admin.asp','login_admin.aspx','login_out/','login_out.asp','login_out.aspx','login_user.asp','login_user.aspx','loginsuper.asp','loginsuper.aspx','super1.asp','loginsuper.asp','loginsuper.aspx','super1.aspx','super_index.asp','super_index.aspx','super_login.asp','super_login.aspx','super_join.asp','super_join.aspx','supermanager.asp','supermanager.aspx','superman.asp','superman.aspx','superuser.asp','superuser.aspx','supervise/Login.asp','supervise/Login.aspx','letmein.asp','letmein.aspx','superuser.asp','superuser.aspx','sysadm.asp','sysadm.aspx','access.asp','access.aspx',
'mn-admin/index.asp','mn-admin/index.aspx','mn-admin/login.asp','mn-admin/login.aspx','mn-admin/admin.asp','mn-admin/admin.aspx','security/','admini/','letmein','admin_user/','admin_users','0admin/login.asp','0admin/login.aspx','0manager/admin.asp','0manager/admin.aspx','a_main.asp','a_main.aspx','aaa.asp','aaa.aspx','aadmin/','abc/','acct/login.asp','acct/login.aspx','d_admin/admin_login.asp','d_admin/admin_login.aspx',
'ad_login/','ad_login.asp','ad_login.aspx','add_admin/','add_user/','addfile.asp','addfile.aspx','addmember/','addmember.asp','addmember.aspx','adduser/','adduser.asp','adduser.aspx','admanage/','adminpro/','adminmember.asp','adminmember.aspx','adminmember/','admins/','adsystem/index.asp','adsystem/index.aspx','adsystem/login.asp','adsystem/login.aspx','adsystem/admin.asp','adsystem/admin.aspx','myadmin/','myadmin/login.asp','myadmin/login.aspx','myadmin/admin.asp','myadmin/admin.aspx','my-admin/','my-admin/admin.asp','my-admin/admin.aspx','my-admin/login.asp','my-admin/login.aspx','yonetim.asp','yonetim.aspx','indy_admin/','liveUser_admin/','lotus_domino_admin/','p/w/','psuser/','personal/','accounts/',
'acesso/','acesso.asp','acesso.aspx','banneradmin/','cadmins/','ccms/','ccms/index.asp','ccms/index.aspx','ccms/login.asp','ccms/login.aspx','ccp14admin/','cms/','config/','configuration/','configure/','customer_login/','dir-login/','directadmin/','donos/','edit/','ezsqliteadmin/','fileadmin/','formslogin/','funcoes/','globes_admin/','hpwebjetadmin/','irc-macadmin/','login-us/','login-redirect/','macadmin/','maintenance/','manage/','management.asp','management.aspx',
'manager/','manuallogin/','members/','members.asp','membro/','membros/','memlogin/','meta_login/','modcp/','navsiteadmin/','newsadmin/','newsadmin.asp','newsadmin.aspx','news-admin/','news-admin.asp','news-admin.aspx','funadmin/','fun-admin/','funadmin.asp/','funadmin.aspx/','fun-admin.asp','fun-admin.aspx','nsw/admin/login.asp','nsw/admin/login.aspx','openvpnadmin/','painel/','panelc/','paneldecontrol/','passe/','password/','pgadmin/','asp/','aspx/','aspsqliteadmin/','aspxsqliteadmin/','aspldapadmin/','aspxldapadmin/','platz_login/','power_user/',
'processlogin/','project-admins/','pureadmin/','radmind-1/','raiz/','rcLogin/','registration/','root/','root/login.asp','root/login.aspx','root/admin.asp','root/admin.aspx','roots/','roots/admin.asp','roots/admin.aspx','roots/login.asp','roots/login.aspx','saff/','secret/','secrets/','secure/','senha/','senhas/','server_admin_small/','showlogin/','sff/','simplelogin/','sistema/','siteadmin/admin.asp','siteadmin/admin.aspx','smblogin/','sql-admin/','asp-admin/','aspx-admin/','ss_vms_admin_sm/','sshadmin/','staradmin/','sub-login/','superman/','administrator/?h','GeneratedItems/','sw/','dynpoll/admin/','mailer/admin/','members/memberlogIn.aspx',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews',
'administrator/login.asp','administrator/login.aspx','login1asp','login1aspx',
'0admin/','0manager/','AdminTools/','Clave/','Database_Administration/','FCKeditor/editor/images/anchor.gif','server.asp','server.aspx','Server/','ServerAdministrator/','Sing/','Super-Admin/','SysAdmin/','SysAdmin2/','UserLogin/','access/','acct_login/','admcp/','admin.xhtml','admin1.asp','admin1.aspx',
'admin4_account/','admin4_colon/','admincontrol/','admincp/','administer/','administr8/','administracao/','administratie/','administration.asp','administration.aspx','administratie.asp','administratie.aspx','administration/','administratoraccounts/','administrators.asp','administrators.aspx','administrators/','administrivia/',
'modiriyat/','modiriat/','modiryat/','modiriyat/modiriyat.asp','modiriyat/modiriyat.aspx','modiriyat/modiriat.asp','modiriyat/modiriat.aspx','modiriyat/modiryat.asp','modiriyat/modiryat.aspx','modiriat/admin.asp','modiriat/admin.aspx','modiryat/login.asp','modiryat/login.aspx','adminitem.asp','adminitem.aspx','adminitem/',
'adminitems.asp','adminitems.aspx','adminpanel/','adminsite/','admistrador','admistrador/','admon/','autologin/','blogindex/','cgi-bin/login','cgi-bin/loginasp','cgi-bin/loginaspx','cmsadmin/','control.asp','control.aspx','control/','controle','controle/',
'controles','controles/','controlpanel','controlpanel/','cp','cp/','cpanel','cpanel_file/','index.swf','instadmin','instadmin/','irectadmin/','key/','letmein/','log-in/','log_in.asp','log_in.aspx','log_in/','login','login-ir/','login-fa/',
'login1','login1/','login_admin','login_admin/','login_db/','login_out','login_user','login_user/','loginerror/','loginflat/','loginok/','loginsave/','loginsuper','loginsuper/','logo_sysadmin/','logout/','hall7/admin.asp','hall7/admin.aspx','supermanager','supermanager/','logoutasp','logoutaspx','manage.asp',
'manage.aspx','management/','manager.asp','manager.aspx','member/','moderatorcp','modules/admin/','net/','news_detail.asp','news_detail.aspx','not/','noticias/','pages/admin/','panel.asp','panel.aspx','panel/','phppgadmin/','radmind/','raiz','roots','siteadmin/','super','super/','super1','super1/','super1asp',
'super1aspx','super_index','super_index/','super_indexasp','super_indexaspx','super_loginasp','super_loginaspx','superasp','superaspx','superasp/','superaspx/','superman','supermanagerasp','supermanageraspx','supermanagerasp/','supermanageraspx/','supermanasp','supermanaspx','supermanasp/','supermanaspx/','super.asp','super.aspx',
'superuser','superuser/','superuserasp','superuseraspx','superuserasp/''superuseraspx/','supervise/','supervise/Login','supervise/Loginasp','supervise/Loginaspx','supervise/Loginasp/','supervise/Loginaspx/','supervisor/','support_login/','sys-admin/','sysadm/','sysadmins/','system-administration/',
'typo3/','usager/','user/','useradmin/','username/','users.asp','users.aspx','users/','usr/','usuario','utility_login/','uvpanel/','vadmind/','vmailadmin/','vorod/','voroud/','vorud/','webadmin','webmaster/','websvn/','wizmysqladmin/','wp-admin','wp-login/','xlogin/']

    cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews']

    js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','panel/js/jquery.maskedinput.js',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews',
'js/%20id=','js/jquery-1.4.2.js','js/url.slice(0,off)']

    cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews','cgi-bin/loginphp']

    brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf',
'newposts/','*subaction=userinfo','*subaction=newposts','*do=lostpassword','*do=addnews']
    
    anytype = ['Server.','Server.%EXT%','acceso.','acceso.%EXT%','accounts.','accounts.%EXT%','adm.','adm.%EXT%','adm_auth.','adm_auth.%EXT%','admin-login.','admin-login.%EXT%','admin.','admin.%EXT%','admin/account.','admin/account.%EXT%','admin/admin-login.',
'admin/admin-login.%EXT%','admin/admin.','admin/admin.%EXT%','admin/adminLogin.','admin/adminLogin.%EXT%','admin/admin_login.','admin/admin_login.%EXT%','admin/controlpanel.','admin/controlpanel.%EXT%',
'admin/cp.','admin/cp.%EXT%','admin/home.','admin/home.%EXT%','admin/login.','admin/login.%EXT%','admin1.','admin1.%EXT%','admin2.','admin2.%EXT%','admin_area.','admin_area.%EXT%','admin_area/admin.',
'admin_area/admin.%EXT%','admin_area/login.','admin_area/login.%EXT%','admin_login.','admin_login.%EXT%','admincontrol.','admincontrol.%EXT%','admincp/login.','admincp/login.%EXT%','administr8.','administr8.%EXT%','administration.','administration.%EXT%','administrator.',
'administrator.%EXT%','administrator/account.','administrator/account.%EXT%','administrator/login.','administrator/login.%EXT%','administratorlogin.','administratorlogin.%EXT%','administrators.','administrators.%EXT%','adminitem.','adminitem.%EXT%','adminitems.','adminitems.%EXT%','adminlogin.','adminlogin.%EXT%','adminpanel.','adminpanel.%EXT%','admins.','admins.%EXT%',
'affiliate.','affiliate.%EXT%','auth.','auth.%EXT%','authadmin.','authadmin.%EXT%','authenticate.','authenticate.%EXT%','authentication.','authentication.%EXT%','authuser.','authuser.%EXT%','autologin.','autologin.%EXT%',
'bb-admin/admin.','bb-admin/admin.%EXT%','blog/wp-login.','blog/wp-login.%EXT%','wp-login.%EXT%','wp-login.','cgi-bin/login.%EXT%','check.','check.%EXT%','checkadmin.','checkadmin.%EXT%','checklogin.','checklogin.%EXT%',
'checkuser.','checkuser.%EXT%','cmsadmin.','cmsadmin.%EXT%','control.','control.%EXT%','controlpanel.','controlpanel.%EXT%','cp.','cp.%EXT%','fileadmin.','fileadmin.%EXT%','isadmin.','isadmin.%EXT%','letmein.',
'letmein.%EXT%','log-in.','log-in.%EXT%','log_in.','log_in.%EXT%','login%EXT%','login.','login.%EXT%','login1.','login1.%EXT%','login_admin.','login_admin.%EXT%','login_out.','login_out.%EXT%','login_user.','login_user.%EXT%',
'loginsuper.','loginsuper.%EXT%','logout.','logout.%EXT%','manage.%EXT%','management.%EXT%','manager.%EXT%','member.%EXT%','memberadmin.%EXT%','members.%EXT%','members.','modelsearch/login.%EXT%','modelsearch/login.','moderator.','moderator.%EXT%','moderator/admin.','moderator/admin.%EXT%','moderator/login.','moderator/login.%EXT%','pages/admin/admin-login.','pages/admin/admin-login.%EXT%',
'panel-administracion/login.','panel-administracion/login.%EXT%','panel.','panel.%EXT%','processlogin.','processlogin.%EXT%','relogin.','relogin.%EXT%','sign-in.','sign-in.%EXT%','sign_in.','sign_in.%EXT%','signin.','signin.%EXT%','siteadmin.','siteadmin.%EXT%','super%EXT%','super.%EXT%','super.','super1%EXT%','super1.%EXT%','super1.','super_index%EXT%','super_index.%EXT%','super_index.',
'super_login%EXT%','super_login.','super_login.%EXT%','superman%EXT%','superman.%EXT%','superman.','superuser%EXT%','superuser.','superuser.%EXT%','supervise/Login%EXT%','supervise/Login.%EXT%','supervise/Login.','sysadm.','sysadm.%EXT%','sysadmin.','sysadmin.%EXT%','ur-admin.','ur-admin.%EXT%','user.','user.%EXT%','user/admin.','user/admin.%EXT%','userlogin.','userlogin.%EXT%','users.','users.%EXT%',
'users/admin.','users/admin.%EXT%','vorod.','vorod.%EXT%','vorud.','voroud.','voroud.%EXT%','vorud.%EXT%','webadmin.','webadmin.%EXT%','webmaster.','webmaster.%EXT%','yonetici.','yonetici.%EXT%','yonetim.','yonetim.%EXT%']
	
    try:
        site = raw_input("Enter Web Site For Scan: (Example: www.victim.com)")
        site = site.replace("http://","")
        print ("\tChecking website " + site + "...")
        conn = httplib.HTTPConnection(site)
        conn.connect()
        print "\t[$] Yes... Server is On-line."
    except (httplib.HTTPResponse, socket.error) as Exit:
        raw_input("\t [!] Oops Error occurred, Server off-line or invalid URL")
        exit()
    print "Enter site source code:\n"
    print "1 PHP"
    print "2 ASP And ASPX"
    print "3 CFM"
    print "4 JS"
    print "5 CGI"
    print "6 BRF"
    print "7 Any Type"
    print "\nPress Enter Website Type For Scan! (Example: Enter 1 For Scan PHP Website\n"
    code=input("> ")
        
    if code==1:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in php:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("[/] The Game Over; Press Enter to Exit")


    if code==2:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in asp:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("The Game Over; Press Enter to Exit")

    if code==3:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in cfm:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("The Game Over; Press Enter to Exit")

    if code==4:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in js:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("The Game Over; Press Enter to Exit")

    if code==5:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in cgi:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("The Game Over; Press Enter to Exit")

    if code==6:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in brf:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("The Game Over; Press Enter to Exit")
		
    if code==7:
        print("\t [+] Scanning " + site + "...\n\n")
        for admin in anytype:
            admin = admin.replace("\n","")
            admin = "/" + admin
            host = site + admin
            print ("\t [#] Checking " + host + "...")
            connection = httplib.HTTPConnection(site)
            connection.request("GET",admin)
            response = connection.getresponse()
            var2 = var2 + 1
            if response.status == 200:
                var1 = var1 + 1
                print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
                raw_input("Press enter to continue scanning.\n")
            elif response.status == 404:
                var2 = var2
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
            else:
                print "%s %s %s" % (host, " Interesting response:", response.status)
            connection.close()
        print("\n\nCompleted \n")
        print var1, " Admin pages found"
        print var2, " total pages scanned"
        raw_input("[/] The Game Over; Press Enter to Exit")
		
except (httplib.HTTPResponse, socket.error):
    print "\n\t[!] Session Cancelled; Error occurred. Check internet settings"
except (KeyboardInterrupt, SystemExit):
    print "\n\t[!] Session cancelled"
