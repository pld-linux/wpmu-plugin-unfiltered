%define		plugin	unfiltered
Summary:	unfiltered-html capability for WordPress
Name:		wpmu-plugin-%{plugin}
Version:	1.2
Release:	1
License:	Unknown, but it safe to assume, it's under wordpress' license (GPL)
Group:		Applications/Publishing
URL:		http://wordpress.org/extend/plugins/unfiltered-mu/
Source0:	http://downloads.wordpress.org/plugin/unfiltered-mu.zip
# Source0-md5:	323784d2024f2d8e6e45113f3313a456
BuildRequires:	unzip
Requires:	wpmu >= 2.8.4
Obsoletes:	wordpress-plugin-unfiltered-mu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins

%description
Unfiltered MU gives Administrators and Editors the unfiltered_html
capability. This prevents WordPress MU from stripping <iframe>,
<embed>, etc. from these users' posts. Authors and Contributors do not
get this capability for security reasons.

Warning! This is a very dangerous plugin to activate if you have
untrusted users on your site. Any user could add Javascript code to
steal the login cookies of any visitor who runs a blog on the same
site. The rogue user can then inpersonate any of those users and wreak
havoc. If all you want is to display videos on your WordPress MU
blogs, use Viper's Video Quicktags or any of the other video plugins
on WordPress.org.

The plugin can either be used globally for your entire MU site, or it
can be applied on a blog-by-blog basis.

%prep
%setup -q -n unfiltered-mu

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pluginsdir}
cp -a unfiltered-mu.php $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%{pluginsdir}/unfiltered-mu.php
