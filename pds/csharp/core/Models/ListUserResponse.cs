// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * List user response
     */
    public class ListUserResponse : TeaModel {
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<BaseUserResponse> Items { get; set; }

        /// <summary>
        /// 翻页标记
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
