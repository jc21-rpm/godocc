%define debug_package %{nil}

%global gh_user inancgumus

Name:           godocc
Version:        0.0.1
Release:        1%{?dist}
Summary:        Like "go doc" but with colors.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
BuildRequires:  git golang

%description
godocc comes with many colors! Configure the color of the output by setting the following env variable:
$ GODOCC_STYLE="dracula"
My favorite styles: dracula, monokai, fruity, native, paraiso-dark, pygments, rainbow_dash, rrt, solarized-dark, swapoff, vim.
Other styles: abap, algol, arduino, autumn, borland, bw, colorful, emacs, friendly, github, igor, lovelace, manni,
monokailight, murphy, paraiso-light, pastie, perldoc, solarized-light256, solarized-light, tango, trac, vs, xcode.

%prep
#wget https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
wget https://github.com/inancgumus/godocc/archive/master.zip
unzip master.zip
#tar xzf v%{version}.tar.gz
mkdir -p %{_builddir}/src/github.com/%{gh_user}/
cd %{_builddir}/src/github.com/%{gh_user}/
#ln -snf %{_builddir}/%{name}-%{version} %{name}
ln -snf %{_builddir}/%{name}-master %{name}
cd %{name}

%build
export GOPATH="%{_builddir}"
export PATH=$PATH:"%{_builddir}"/bin
cd %{_builddir}/src/github.com/%{gh_user}/%{name}
export GO111MODULE=on
go build -o %{_builddir}/bin/%{name} main.go

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Wed Dec 11 2019 Jamie Curnow <jc@jc21.com> 0.0.1-1
- v0.0.1, untagged github master code

