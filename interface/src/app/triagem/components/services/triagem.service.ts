import { ListarDiagnosticoResponse, ListarDiagnosticoModel } from '../models/services/listar-diagnosticos.response';
import { Injectable } from '@angular/core';
import { ListarSintomasRequest } from '../models/services/listar-sintomas.request';
import { ListarDiagnosticosRequest } from '../models/services/listar-diagnosticos.request';
import { ListarSintomasResponse, ListarSintomasModel } from '../models/services/listar-sintomas.response';

@Injectable({
    providedIn: 'root',
  })
export class TriagemService {
    constructor(
      ) {
      }

      public async ListarDiagnostico(): Promise<ListarDiagnosticoResponse> {
        const item1: ListarDiagnosticoModel = {
            idDiagnostico: 1,
            tituloDiagnostico: "Alteração do Estado Neurológico"
          }
    
        const item2: ListarDiagnosticoModel = {
            idDiagnostico: 2,
            tituloDiagnostico: "Anafilaxia e Reação Alérgica"
          }

        const listarDiagnosticoResponse : ListarDiagnosticoResponse = {
          data: [item1, item2],
          errors: [],
          success: true
        };

        return listarDiagnosticoResponse;
      }

      public async ListarSintomas(request: ListarSintomasRequest): Promise<ListarSintomasResponse>{
        const item1: ListarSintomasModel = {
          idSintoma: 1,
          descricaoSintoma: `Déficit cognitivo – agitação, letargia, confusão; convulsão, paralisia,
          sonolência, coma (Glasgow 9 a 13)`
        }

        const item2: ListarSintomasModel = {
          idSintoma: 2,
          descricaoSintoma: `PA > 180/ 110`
        }

        const item3: ListarSintomasModel = {
          idSintoma: 3,
          descricaoSintoma: `Febre`
        }

        const response: ListarSintomasResponse = {
          data: [item1, item2, item3],
          errors: [],
          success: true
        }

        return response;
      }
    
}