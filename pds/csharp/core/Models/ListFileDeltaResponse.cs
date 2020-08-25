// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * list file op response
     */
    public class ListFileDeltaResponse : TeaModel {
        /// <summary>
        /// cursor
        /// </summary>
        [NameInMap("cursor")]
        [Validation(Required=false)]
        public string Cursor { get; set; }

        /// <summary>
        /// has_more
        /// </summary>
        [NameInMap("has_more")]
        [Validation(Required=false)]
        public bool? HasMore { get; set; }

        /// <summary>
        /// items
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<FileDeltaResponse> Items { get; set; }

    }

}
