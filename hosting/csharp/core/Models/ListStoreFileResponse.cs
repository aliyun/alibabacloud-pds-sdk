// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * List storage file
     */
    public class ListStoreFileResponse : TeaModel {
        /// <summary>
        /// items
        /// file list
        /// </summary>
        [NameInMap("items")]
        [Validation(Required=false)]
        public List<StoreFile> Items { get; set; }

        [NameInMap("next_marker")]
        [Validation(Required=false)]
        public string NextMarker { get; set; }

    }

}
