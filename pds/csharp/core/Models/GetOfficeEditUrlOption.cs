// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * GetOfficeEditUrlOption 权限控制
     */
    public class GetOfficeEditUrlOption : TeaModel {
        /// <summary>
        /// Copy
        /// </summary>
        [NameInMap("copy")]
        [Validation(Required=false)]
        public bool? Copy { get; set; }

        [NameInMap("readonly")]
        [Validation(Required=false)]
        public bool? Readonly { get; set; }

    }

}
