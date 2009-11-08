%define module cabalrpmdeps

Name: haskell-%{module}
Version: 0.0.4
Release: %mkrel 3
Summary: Tools to build rpm dependencies from Cabal
Group: Development/Other
License: LGPL
Url: http://nanardon.zarb.org/darcsweb/darcsweb.cgi?r=haskell-CabalRpmDeps;a=summary
Source: http://hackage.haskell.org/packages/archive/%{module}/%{module}-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
Provides: haskell(%{module}) = %version
# We don't use it to avoid dependencies loop !!
# BuildRequires: haskell-macros

%description
Tools to build rpm dependencies from Cabal

%package -n %{module}
Summary: Tools to build rpm dependencies from Cabal
Group: Development/Other

%description -n %{module}
Tools to build rpm dependencies from Cabal

%prep
%setup -q -n %{module}-%{version}

%build
runhaskell Setup.hs configure --prefix=%{_prefix}
runhaskell Setup.hs build
runhaskell Setup.hs haddock

%check
runhaskell Setup.hs test

%install
runhaskell Setup.hs copy --destdir=%{buildroot}

runhaskell Setup.hs   register --gen-script
runhaskell Setup.hs unregister --gen-script

rm -fr %{buildroot}/%_datadir/*

%triggerin -f   register.sh -- ghc
%triggerun -f unregister.sh -- ghc

%files
%defattr(-,root,root)
%doc dist/doc/html
%_libdir/*

%files -n %{module}
%defattr(-,root,root)
%_bindir/*

%clean
rm -fr %buildroot


