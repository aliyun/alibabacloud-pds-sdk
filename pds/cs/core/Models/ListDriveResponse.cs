// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list drive response
     */
    public class ListDriveResponse : TeaModel {
        /// <summary>
        /// Drive 列表
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<BaseDriveResponse> Items { get; set; }

        /// <summary>
        /// 翻页标记
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
