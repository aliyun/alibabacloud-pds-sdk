// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list file activity response
     */
    public class ListFileActivityResponse : TeaModel {
        /// <summary>
        /// Activities
        /// </summary>
        [NameInMap("activities")]
        [Validation(Required=false)]
        public List<FileActivity> Activities { get; set; }

        /// <summary>
        /// NextMarker
        /// </summary>
        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
