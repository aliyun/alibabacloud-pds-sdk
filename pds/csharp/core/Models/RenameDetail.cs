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
    public class RenameDetail : TeaModel {
        /// <summary>
        /// NewName
        /// </summary>
        [NameInMap("new_name")]
        [Validation(Required=false)]
        public string NewName { get; set; }

        /// <summary>
        /// OldName
        /// </summary>
        [NameInMap("old_name")]
        [Validation(Required=false)]
        public string OldName { get; set; }

    }

}
