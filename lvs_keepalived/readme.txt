1.用vagrant搭建4台服务器（DR1 DR2 app1 app2）
2.安装lvs ipvsadm keepalived
3.master和slave分别配置keepalived.conf
4.realserver上配置启动脚本
   chkconfig keepalived on
5.测试
   ipvsadm -Ln
   ip addr


http://www.linuxvirtualserver.org/docs/ha/keepalived.html
