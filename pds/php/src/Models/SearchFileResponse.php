<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\PDS\SDK\Models\BaseCCPFileResponse;

/**
 * search file response
 */
class SearchFileResponse extends Model {
    protected $_name = [
        'items' => 'items',
        'nextMarker' => 'next_marker',
        'totalCount' => 'total_count',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->items) {
            $res['items'] = [];
            if(null !== $this->items && is_array($this->items)){
                $n = 0;
                foreach($this->items as $item){
                    $res['items'][$n++] = null !== $item ? $item->toMap() : $item;
                }
            }
        }
        if (null !== $this->nextMarker) {
            $res['next_marker'] = $this->nextMarker;
        }
        if (null !== $this->totalCount) {
            $res['total_count'] = $this->totalCount;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return SearchFileResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['items'])){
            if(!empty($map['items'])){
                $model->items = [];
                $n = 0;
                foreach($map['items'] as $item) {
                    $model->items[$n++] = null !== $item ? BaseCCPFileResponse::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['next_marker'])){
            $model->nextMarker = $map['next_marker'];
        }
        if(isset($map['total_count'])){
            $model->totalCount = $map['total_count'];
        }
        return $model;
    }
    /**
     * @description items
     * @example 
     * @var BaseCCPFileResponse[]
     */
    public $items;

    /**
     * @description next_marker
     * @example NWQ1YmI4MjA0ZGU1ZWNjYzAzODM0ZDVkODlkMWJiMzcyNzM1NTU4OA
     * @var string
     */
    public $nextMarker;

    /**
     * @description total_count
     * @var int
     */
    public $totalCount;

}
