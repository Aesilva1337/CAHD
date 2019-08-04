import { Component, OnInit } from '@angular/core';
import { TriagemService } from '../services/triagem.service';
import { DiagnosticoModel } from '../models/components/diagnostico.model';

@Component({
    selector: 'app-sintomas',
    templateUrl: './sintomas.component.html',
    styleUrls: ['./sintomas.component.scss']
  })
  export class SintomasComponent implements OnInit {
    constructor(
      private triagemService: TriagemService,
    ) {
    }

    public listSintomas: DiagnosticoModel[] = [];

    async ngOnInit() {
      const response = await this.triagemService.ListarDiagnostico();
      response.data.forEach(diag => this.listSintomas.push({
        id: diag.idDiagnostico,
        titulo: diag.tituloDiagnostico,
        descricao: diag.descDiagnostico
      }));
    }

  }