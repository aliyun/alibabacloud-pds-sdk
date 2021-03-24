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
    public class MoveDetail : TeaModel {
        /// <summary>
        /// SrcParentFileID
        /// </summary>
        [NameInMap("src_parent_file_id")]
        [Validation(Required=false)]
        public string SrcParentFileId { get; set; }

        /// <summary>
        /// TgtParentFileID
        /// </summary>
        [NameInMap("tgt_parent_file_id")]
        [Validation(Required=false)]
        public string TgtParentFileId { get; set; }

    }

}
