<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\Hosting\SDK\Models;

use AlibabaCloud\Tea\Model;

use Aliyun\Hosting\SDK\Models\BaseDomainResponse;

/**
 * list domain response
 */
class ListDomainsResponse extends Model {
    protected $_name = [
        'items' => 'items',
        'nextMarker' => 'next_marker',
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
        return $res;
    }
    /**
     * @param array $map
     * @return ListDomainsResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['items'])){
            if(!empty($map['items'])){
                $model->items = [];
                $n = 0;
                foreach($map['items'] as $item) {
                    $model->items[$n++] = null !== $item ? BaseDomainResponse::fromMap($item) : $item;
                }
            }
        }
        if(isset($map['next_marker'])){
            $model->nextMarker = $map['next_marker'];
        }
        return $model;
    }
    /**
     * @description domain 列表
     * @example 
     * @var BaseDomainResponse[]
     */
    public $items;

    /**
     * @description 下次分页查询游标
     * @example NWQ1YmI4MjA0ZGU1ZWNjYzAzODM0ZDVkODlkMWJiMzcyNzM1NTU4OA
     * @var string
     */
    public $nextMarker;

}
