// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class CreateDetail : TeaModel {
        /// <summary>
        /// CreateType
        /// </summary>
        [NameInMap("create_type")]
        [Validation(Required=false)]
        public string CreateType { get; set; }

        /// <summary>
        /// SrcFileID
        /// </summary>
        [NameInMap("src_file_id")]
        [Validation(Required=false)]
        public string SrcFileId { get; set; }

    }

}
