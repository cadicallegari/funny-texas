package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
)

type Record struct {
	Contacto struct {
		NumeroTelefono    string `json:"numeroTelefono"`
		SitioInternet     string `json:"sitioInternet"`
		CorreoElectronico string `json:"correoElectronico"`
	} `json:"contacto"`
	ID                       string `json:"id"`
	TipoEstablecimiento      string `json:"tipoEstablecimiento"`
	DescricionEstratoOcupado string `json:"descricionEstratoOcupado"`
	NombreUnidadEconomica    string `json:"nombreUnidadEconomica"`
	FechaIncorporacionDENUE  struct {
		Mes int `json:"mes"`
		Ano int `json:"ano"`
	} `json:"fechaIncorporacionDENUE"`
	ClasseActividad struct {
		Codigo string `json:"codigo"`
		Nombre string `json:"nombre"`
	} `json:"classeActividad"`
	RazonSocial string `json:"razonSocial"`
	Direciones  struct {
		ClaveLocalidad           string `json:"claveLocalidad"`
		EdificioPiso             string `json:"edificioPiso"`
		ClaveMunicipio           string `json:"claveMunicipio"`
		NombreAsentamientoHumano string `json:"nombreAsentamientoHumano"`
		TipoAsentamientoHumano   string `json:"tipoAsentamientoHumano"`
		Municipio                string `json:"municipio"`
		NumeroLocal              string `json:"numeroLocal"`
		Localidad                string `json:"localidad"`
		Manzana                  string `json:"manzana"`
		CodigoPostal             string `json:"codigoPostal"`
		LetraInterior            string `json:"letraInterior"`
		LetraExterior            string `json:"letraExterior"`
		AreaGeoestadistica       string `json:"areaGeoestadistica"`
		ClaveEntidad             string `json:"claveEntidad"`
		TipoCentroComercial      string `json:"tipoCentroComercial"`
		Vialidades               []struct {
			Tipo   string `json:"tipo"`
			Nombre string `json:"nombre"`
		} `json:"vialidades"`
		CorredorIndustrialOuMercadoPublico string `json:"corredorIndustrialOuMercadoPublico"`
		Latitud                            string `json:"latitud"`
		EntidadFederativa                  string `json:"entidadFederativa"`
		NumeroInterior                     string `json:"numeroInterior"`
		NumeroExteriorKilometro            string `json:"numeroExteriorKilometro"`
		Longitud                           string `json:"longitud"`
		Edificio                           string `json:"edificio"`
	} `json:"direciones"`
}

func toJson(raw string) (Record, error) {
	var r Record
	bytes := []byte(raw)
	err := json.Unmarshal(bytes, &r)
	return r, err
}

func loadJsonFile(path string) ([]Record, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []Record
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		j, _ := toJson(scanner.Text())
		lines = append(lines, j)
	}
	return lines, scanner.Err()
}

func main() {
	// data, _ := loadJsonFile("../resources/small.txt")
	// data, _ := loadJsonFile("../resources/medium.txt")
	data, _ := loadJsonFile("../resources/large.txt")
	fmt.Println(len(data))
}
