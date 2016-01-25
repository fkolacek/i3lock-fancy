Name:   i3lock-fancy
Version:  1.0
Release:  1%{?dist}
Summary:  Customized i3lock-fancy packed to RPM
Packager: Frantisek Kolacek <fkolacek@redhat.com>
Group:    User Interface/Desktops
License:  MIT
URL:    https://github.com/fkolacek/i3lock-fancy
Source0:  i3lock-fancy-1.0.tgz

Requires: i3lock scrot ImageMagick

%description
Custom i3lock-fancy configuration packed to RPM package.

%prep
%setup -q

%clean
rm -rf %{buildroot}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/bin

install i3lock-fancy %{buildroot}/usr/local/bin/i3lock-fancy
chmod 755 %{buildroot}/usr/local/bin/i3lock-fancy

%files
/usr/local/bin/i3lock-fancy

%changelog
* Mon Jan 25 2016 Frantisek Kolacek <fkolacek@redhat.com> 1.0-1
--First repack
