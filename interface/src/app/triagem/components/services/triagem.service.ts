import { ListarDiagnosticoResponse, ListarDiagnosticoModel } from '../models/services/listar-diagnosticos.response';
import { Injectable } from '@angular/core';

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
            tituloDiagnostico: "Diagnostico 1",
            descDiagnostico: "Descrição diagnostico 1"
          }
    
        const item2: ListarDiagnosticoModel = {
            idDiagnostico: 2,
            tituloDiagnostico: "Diagnostico 2",
            descDiagnostico: "Descrição diagnostico 2"
          }

        const listarDiagnosticoResponse : ListarDiagnosticoResponse = {
          data: [item1, item2],
          errors: [],
          success: true
        };

        return listarDiagnosticoResponse;
      }
    
}